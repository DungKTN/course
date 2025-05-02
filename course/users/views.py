from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import User
from .serializers import Userserializers
from .services import create_user, update_user, delete_user, get_users, get_user_by_id

class UserListView(APIView):
    def get(self, request):
        users = get_users()
        serializer = Userserializers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCreateView(APIView):
    def post(self, request):
        try:
            user = create_user(request.data)
            return Response(Userserializers(user).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = get_user_by_id(user_id=user_id)
            serializer = Userserializers(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, user_id):
        try:
            updated_user = update_user(user_id, request.data)
            return Response(Userserializers(updated_user).data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        try:
            result = delete_user(user_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_404_NOT_FOUND)
