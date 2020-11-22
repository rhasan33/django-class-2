from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class IsRestaurantAdmin(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.groups.filter(name='RestaurantAdmin').exists()
