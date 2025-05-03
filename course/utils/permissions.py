# utils/permissions.py
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from django.conf import settings
import jwt
JWT_SECRET = settings.SECRET_KEY
def RolePermissionFactory(roles):
    class _RolePermission(BasePermission):
        def has_permission(self, request, view):
            print("Reqsuest Headers:")
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise AuthenticationFailed("Thiếu token hoặc sai định dạng.")

            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(token, JWT_SECRET, algorithms="HS256")
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed("Token hết hạn.")
            except jwt.InvalidTokenError:
                raise AuthenticationFailed("Token không hợp lệ.")

            user_type = payload.get("user_type")
            if user_type not in (roles if isinstance(roles, list) else [roles]):
                raise PermissionDenied("Bạn không có quyền truy cập.")

            request.jwt_payload = payload
            return True

    return _RolePermission
