from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Review
from courses.models import Course
from .serializers import ReviewSerializer
from .services import (
    create_review,
    update_review,
    delete_review,
    get_reviews_by_course,
    get_review_by_id,
    count_reviews_by_course,
    count_like_review
)
from utils.permissions import RolePermissionFactory

class ReviewListView(APIView):
    def get(self, request):
        try:
            reviews = get_reviews_by_course(request.query_params.get('course_id'))
            return Response(reviews, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        try:
            review = create_review(request.data)
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, review_id):
        try:
            updated_review = update_review(review_id, request.data)
            return Response(ReviewSerializer(updated_review).data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, review_id):
        try:
            result = delete_review(review_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_404_NOT_FOUND)

class ReviewDetailView(APIView):
    def get(self, request, review_id):
        try:
            review = get_review_by_id(review_id)
            return Response(review, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)
