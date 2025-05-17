# utils/permissions.py
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from django.conf import settings
import jwt
from users.models import User
JWT_SECRET = settings.SECRET_KEY
def RolePermissionFactory(roles):
    class _RolePermission(BasePermission):
        def has_permission(self, request, view):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise AuthenticationFailed("Thiếu token hoặc sai định dạng.")
            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(token, JWT_SECRET, algorithms="HS256")
                user = User.objects.get(user_id=payload["user_id"])
                if user.status == User.StatusChoices.BANNED:
                    raise AuthenticationFailed("Tài khoản bị cấm.")
                if user.status == User.StatusChoices.INACTIVE:
                    raise AuthenticationFailed("Tài khoản chưa kích hoạt.")
            except User.DoesNotExist:
                raise AuthenticationFailed("Người dùng không tồn tại.")
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed("Token hết hạn.")
            except jwt.InvalidTokenError:
                raise AuthenticationFailed("Token không hợp lệ.")
            user.user_type = payload.get("user_type")
            if user.user_type not in (roles if isinstance(roles, list) else [roles]):
                raise PermissionDenied("Bạn không có quyền truy cập.")
            request.jwt_payload = payload
            return True

    return _RolePermission
