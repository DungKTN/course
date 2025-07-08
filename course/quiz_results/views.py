from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_quiz_result,
    get_quiz_result_by_id,
    get_all_quiz_results,
    update_quiz_result,
    delete_quiz_result,
    get_quiz_results_by_enrollment,
)

class QuizResultListView(APIView):
    def post(self, request):
        try:
            data = request.data
            quiz_result = create_quiz_result(data)
            return Response(quiz_result, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        try:
            if 'enrollment_id' in request.query_params:
                enrollment_id = request.query_params.get('enrollment_id')
                quiz_results = get_quiz_results_by_enrollment(enrollment_id)
                return Response(quiz_results, status=status.HTTP_200_OK)
            elif 'quiz_result_id' in request.query_params:
                quiz_result_id = request.query_params.get('quiz_result_id')
                quiz_result = get_quiz_result_by_id(quiz_result_id)
                return Response(quiz_result, status=status.HTTP_200_OK)
            else:
                quiz_results = get_all_quiz_results()
                return Response(quiz_results, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, quiz_result_id):
        try:
            quiz_result = update_quiz_result(quiz_result_id, request.data)
            return Response(quiz_result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, quiz_result_id):
        try:
            result = delete_quiz_result(quiz_result_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)