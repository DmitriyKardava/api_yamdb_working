from rest_framework import permissions

from review_user.enums import UserRole


class AdminUserOrReadOnly(permissions.BasePermission):
    message = (f"Доступно только для всех пользователей с безопасными "
               f"запросами или аутентифицированных пользователей с ролью "
               f"{UserRole.ADMIN} для остальных запросов.")

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.role == UserRole.ADMIN
        return False


class AdminPermission(permissions.BasePermission):
    message = f"Доступно только для пользователей с ролью {UserRole.ADMIN}"

    def has_permission(self, request, view):
        if not hasattr(request.user, "role"):
            return False

        return request.user.role == UserRole.ADMIN or request.user.is_superuser
