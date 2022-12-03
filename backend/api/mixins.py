from .permissions import IsStaffEditorPermission
from rest_framework import permissions
class IsStaffEditormixins():
    permission_class=[permissions.IsAdminUser,IsStaffEditorPermission]

class UserQuerySetmixin():
    user_filed='user'
    def get_queryset(self):
        request=self.request
        lookup_field={}
        lookup_field[self.user_filed]=request.user
        qs=super().get_queryset()
        return qs.filter(**lookup_field)