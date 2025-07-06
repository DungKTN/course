from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_qna_answer,
    get_qna_answer_by_id,
    get_qna_answers_by_qna_id,
    update_qna_answer,
    delete_qna_answer,
)

class QnAAnswerListView(APIView):
    def get(self, request):
        try:
            if 'qna_id' in request.query_params:
                qna_id = request.query_params.get('qna_id')
                qna_answers = get_qna_answers_by_qna_id(qna_id)
                return Response(qna_answers, status=status.HTTP_200_OK)
            elif 'answer_id' in request.query_params:
                answer_id = request.query_params.get('answer_id')
                qna_answer = get_qna_answer_by_id(answer_id)
                return Response(qna_answer, status=status.HTTP_200_OK)
            else:
                return Response({"error": "No valid query parameters provided."}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            qna_answer = create_qna_answer(request.data)
            return Response(qna_answer, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, answer_id):
        try:
            updated_qna_answer = update_qna_answer(answer_id, request.data)
            return Response(updated_qna_answer, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_id):
        try:
            result = delete_qna_answer(answer_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)