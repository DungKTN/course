from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_quiz_question,
    get_quiz_questions_by_lesson,
    find_quiz_question_by_id,
    update_quiz_question,
    delete_quiz_question,
    get_all_quiz_questions,
)
from utils.permissions import RolePermissionFactory

class QuizQuestionManagementView(APIView):
    permission_classes = [RolePermissionFactory(['admin', 'instructor'])]

    def post(self, request):
        try:
            quiz_question = create_quiz_question(request.data)
            print("Quiz question created successfully:", quiz_question)
            print("Request data:", request.data)
            return Response(quiz_question, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, lesson_id):
        try:
            quiz_questions = get_quiz_questions_by_lesson(lesson_id)
            return Response(quiz_questions, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, question_id):
        try:
            updated_quiz_question = update_quiz_question(question_id, request.data)
            return Response(updated_quiz_question, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        try:
            response = delete_quiz_question(question_id)
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

class QuizQuestionDetailView(APIView):
    permission_classes = [RolePermissionFactory(['admin', 'instructor'])]

    def get(self, request, question_id):
        try:
            quiz_question = find_quiz_question_by_id(question_id)
            return Response(quiz_question, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

class QuizQuestionListView(APIView):
    permission_classes = [RolePermissionFactory(['admin', 'instructor'])]

    def get(self, request):
        try:
            quiz_questions = get_all_quiz_questions()
            return Response(quiz_questions, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)