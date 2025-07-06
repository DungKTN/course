from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    get_systems_settings,
    get_systems_setting_by_key,
    get_systems_setting_by_admin_id,
    update_systems_setting,
    create_systems_setting,
    delete_systems_setting,
)

class SystemsSettingsView(APIView):
    def get(self, request):
        try:
            if 'setting_key' in request.query_params:
                setting_key = request.query_params.get('setting_key')
                settings = get_systems_setting_by_key(setting_key)
                return Response(settings, status=status.HTTP_200_OK)
            elif 'admin_id' in request.query_params:
                admin_id = request.query_params.get('admin_id')
                settings = get_systems_setting_by_admin_id(admin_id)
                return Response(settings, status=status.HTTP_200_OK)
            else:
                settings = get_systems_settings()
                return Response(settings, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        try:
            settings = create_systems_setting(request.data)
            return Response(settings, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            updated_settings = update_systems_setting(request.data)
            return Response(updated_settings, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            result = delete_systems_setting()
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)