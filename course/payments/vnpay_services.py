from rest_framework.exceptions import ValidationError
from .serializers import PaymentSerializer
from .models import Payment
from datetime import datetime
from courses.models import Course
from django.db import IntegrityError
import hashlib
import hmac
import urllib.parse
from django.http import JsonResponse, HttpRequest
from django.utils import timezone
from datetime import timedelta
import hashlib
import pytz
from datetime import datetime
from payments.vnpay import vnpay
from django.conf import settings
from decimal import Decimal
from instructor_earnings.services import generate_instructor_earnings_from_payment
# from orders.models import Order
# VNPAY cấu hình

vnp_TmnCode = settings.VNPAY_TMN_CODE
vnp_HashSecret = settings.VNPAY_HASH_SECRET_KEY
vnp_Url =  settings.VNPAY_URL
# vnp_Url = 'https://sandbox.vnpayment.vn/paymentv2/vpc
vnp_ReturnUrl = settings.VNPAY_RETURN_URL


def get_payment_url(vnpay_payment_url, params, secret_key):
    # Sắp xếp các tham số theo thứ tự alphabet
    input_data = sorted(params.items())
    query_string = ''
    seq = 0
    for key, val in input_data:
        if seq == 1:
            query_string += "&" + key + '=' + urllib.parse.quote_plus(str(val))
        else:
            seq = 1
            query_string = key + '=' + urllib.parse.quote_plus(str(val))

    hash_value = hmacsha512(secret_key, query_string)
    return vnpay_payment_url + "?" + query_string + '&vnp_SecureHash=' + hash_value

def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def create_vnpay_payment(request: HttpRequest):
    data = request.data if hasattr(request, 'data') else request.GET
    amount = int(data.get('amount')) * 100
    order_id = data.get('order_id') or datetime.now().strftime('%Y%m%d%H%M%S')
    order_desc = data.get('order_desc', f'Thanh toan don hang {order_id}')
    order_type = data.get('order_type', 'other')
    language = data.get('language', 'vn')
    bank_code = data.get('bank_code')
    ip_address = get_client_ip(request)

    # Lấy thời gian hiện tại theo múi giờ GMT+7
    tz = pytz.timezone('Asia/Ho_Chi_Minh')

    params = {
        'vnp_Version': '2.1.0',
        'vnp_Command': 'pay',
        'vnp_TmnCode': vnp_TmnCode,
        'vnp_Amount': str(amount),
        'vnp_CurrCode': 'VND',
        'vnp_TxnRef': order_id,
        'vnp_OrderInfo': order_desc,
        'vnp_OrderType': order_type,
        'vnp_ReturnUrl': vnp_ReturnUrl,  # Bỏ order_id khỏi URL nếu trước đó có
        'vnp_IpAddr': ip_address,
    }
    if language and language != '':
        params['vnp_Locale'] = language
    else:
        params['vnp_Locale'] = 'vn'

    if bank_code and bank_code != '':
        params['vnp_BankCode'] = bank_code
    params['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')
    params['vnp_IpAddr'] = ip_address
    params['vnp_ReturnUrl'] = vnp_ReturnUrl
    params['vnp_CreateDate'] = datetime.now(tz).strftime('%Y%m%d%H%M%S')
    # print(f"Creating VNPAY payment with params: {params}")
    vn_payment_url = get_payment_url(vnp_Url, params, vnp_HashSecret)
    print(vn_payment_url)

    return JsonResponse({'payment_url': vn_payment_url})

def payment_return(request):
    try:
        inputData = request.GET
        if inputData:
            vnp = vnpay()
            vnp.responseData = inputData.dict()
            order_id = inputData['vnp_TxnRef']
            amount = int(inputData['vnp_Amount']) / 100
            order_desc = inputData['vnp_OrderInfo']
            vnp_TransactionNo = inputData['vnp_TransactionNo']
            vnp_ResponseCode = inputData['vnp_ResponseCode']
            vnp_TmnCode = inputData['vnp_TmnCode']
            vnp_PayDate = inputData['vnp_PayDate']
            vnp_BankCode = inputData['vnp_BankCode']
            vnp_CardType = inputData['vnp_CardType']
            if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
                if vnp_ResponseCode == "00":
                    payment = Payment.objects.get(payment_id=order_id)
                    if not payment:
                        print(f"Payment with order_id {order_id} not found.")
                        return JsonResponse({"error": "Payment not found"}, status=404)
                    payment.payment_status = 'completed'
                    if Decimal(payment.total_amount) != Decimal(amount):
                        raise ValidationError("Payment amount mismatch")
                    payment.transaction_id = vnp_TransactionNo
                    payment.payment_date = datetime.now()
                    payment.gateway_response = vnp_ResponseCode
                    payment.payment_gateway = 'vnpay'
                    payment.save()
                    print(f"Payment {order_id} completed successfully.")
                    # Generate instructor earnings from the payment
                    try:
                        generate_instructor_earnings_from_payment(payment)
                    except Exception as e:
                        print(f"Error generating instructor earnings: {str(e)}")
                        return JsonResponse({"error": "Failed to generate instructor earnings"}, status=500)

                else:
                    payment = Payment.objects.get(payment_id=order_id)
                    if not payment:
                        print(f"Payment with order_id {order_id} not found.")
                        return JsonResponse({"error": "Payment not found"}, status=404)
                    payment.payment_status = 'failed'
                    payment.transaction_id = vnp_TransactionNo
                    payment.gateway_response = vnp_ResponseCode
                    payment.save()
                    print(f"Payment {order_id} failed with response code {vnp_ResponseCode}.")
    except Exception as e:
        raise ValidationError(f"Error processing payment return: {str(e)}")
    
    #         if vnp_ResponseCode == "00":
    #             return  {"title": "Kết quả thanh toán",
    #                     "result": "Thành công", "order_id": order_id,
    #                     "amount": amount,
    #                     "order_desc": order_desc,
    #                     "vnp_TransactionNo": vnp_TransactionNo,
    #                     "vnp_ResponseCode": vnp_ResponseCode}
    #         else:
    #             return  {"title": "Kết quả thanh toán",
    #                     "result": "Lỗi", "order_id": order_id,
    #                     "amount": amount,
    #                     "order_desc": order_desc,
    #                     "vnp_TransactionNo": vnp_TransactionNo,
    #                     "vnp_ResponseCode": vnp_ResponseCode}
    #     else:
    #         return {"title": "Kết quả thanh toán",
    #                 "result": "Lỗi", 
    #                 "order_id": order_id, 
    #                 "amount": amount,
    #                 "order_desc": order_desc, "vnp_TransactionNo": vnp_TransactionNo,
    #                 "vnp_ResponseCode": vnp_ResponseCode, "msg": "Sai checksum"}
    # else:
    #     return {"title": "Kết quả thanh toán", "result": ""}



def payment_ipn(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = inputData['vnp_Amount']
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            # Check & Update Order Status in your Database
            # Your code here
            firstTimeUpdate = True
            totalamount = True
            if totalamount:
                if firstTimeUpdate:
                    if vnp_ResponseCode == '00':
                        print('Payment Success. Your code implement here')
                    else:
                        print('Payment Error. Your code implement here')

                    # Return VNPAY: Merchant update success
                    result = JsonResponse({'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    # Already Update
                    result = JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})
            else:
                # invalid amount
                result = JsonResponse({'RspCode': '04', 'Message': 'invalid amount'})
        else:
            # Invalid Signature
            result = JsonResponse({'RspCode': '97', 'Message': 'Invalid Signature'})
    else:
        result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

    return result

# def local_ipn()