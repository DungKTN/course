from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .vnpay_services import create_vnpay_payment
from .vnpay_services import payment_return, payment_ipn
from .services import create_payment

class CreateVnpayPaymentView(APIView):
    def post(self, request):
        try:
            return create_vnpay_payment(request)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class VnpayReturnView(APIView):
    def get(self, request):
        try:
            returnData = payment_ipn(request)
            # Assuming payment_return is a function that handles the return logic
            return Response(returnData, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class CreatePaymentRecordView(APIView):
    def post(self, request):
        try:
            payment = create_payment(request.data)
            return Response(payment, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


