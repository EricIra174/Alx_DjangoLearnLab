from rest_framework.perrmissions import BasePermission
class IsAdminUser(BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user