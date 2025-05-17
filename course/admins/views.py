from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import updateAdminInfo, delete_admin, get_admins, get_admin_by_id, create_admin
from .serializers import AdminSerializer
from utils.permissions import RolePermissionFactory


class AdminManagementView(APIView):
    permission_classes = [RolePermissionFactory("admin")]
    def post(self, request):
        try:
            admin = create_admin(request.data)
            return Response(AdminSerializer(admin).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, admin_id):
        try:
            updated_admin = updateAdminInfo(admin_id, request.data)
            return Response(AdminSerializer(updated_admin).data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, admin_id):
        try:
            result = delete_admin(admin_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_404_NOT_FOUND)

class AdminListView(APIView):
    permission_classes = [RolePermissionFactory("admin")]
    def get(self, request):
        try:
            admins = get_admins()
            return Response(admins, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)

class AdminDetailView(APIView):
    permission_classes = [RolePermissionFactory("admin")]
    def get(self, request, admin_id):
        try:
            admin = get_admin_by_id(admin_id)
            return Response(admin, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)