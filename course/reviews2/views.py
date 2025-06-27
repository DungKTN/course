# reviews/views.py
from utils.decorators import role_required
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
@role_required("student")
def create_review(request):
    return Response({"message": "Bạn đã gửi đánh giá thành công."})
