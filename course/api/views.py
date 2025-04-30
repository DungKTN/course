from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Userserializers
from .models import User
from .services import create_user


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = Userserializers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        serializer = Userserializers(data=request.data)
        if serializer.is_valid():
            user = create_user(serializer.validated_data)
            return Response(Userserializers(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)