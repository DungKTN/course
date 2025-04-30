from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Userserializers
from .models import User
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = Userserializers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.
