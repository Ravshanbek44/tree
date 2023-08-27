from rest_framework import permissions


class IsTreeEkuvchi(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 2


class IsTreeEktiruvchi(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1
