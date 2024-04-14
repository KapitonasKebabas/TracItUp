
from rest_framework import permissions
from .permissions import  IsStaffEditorPermission, IsUserGetPermission, IsUserPostPermission
from rest_framework_simplejwt.authentication import JWTAuthentication as authentication

class StaffEditorPermissionMixin():
    authentication_classes = [
        authentication
    ]
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission
    ]

class UserGetPostPermissionMixin():
    authentication_classes = [
        authentication
    ]
    permission_classes = [
        IsUserPostPermission,
        IsUserGetPermission
    ]

class NoPermissionMixin():
    authentication_classes = []
    permission_classes = []