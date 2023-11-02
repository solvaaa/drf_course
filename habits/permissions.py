from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не владелец этой привычки'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsPublic(BasePermission):
    message = 'Привычка не публичная'

    def has_object_permission(self, request, view, obj):
        return obj.is_public
