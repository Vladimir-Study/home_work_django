from rest_framework import permissions
from advertisements.models import Advertisement


class CustomDeleteAdvertisement(permissions.BasePermission):
    '''
    Удаление чужого обявления
    '''

    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator
