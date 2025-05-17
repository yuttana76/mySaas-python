from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    """
    Custom permission to only allow staff editors to edit or delete a product.
    """
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s']
    }

    # def has_permission(self, request, view):
    #     # if not request.user.username == 'admin':
    #     #     return False
        

    #     # if not request.user.is_authenticated:
    #     #     return False

    #     # if not request.user.is_staff:
    #     #     return False
    #     return super().has_permission(request, view)


    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())

    #     if user.is_staff:
    #         if user.has_perm('products.add_product'):
    #             return True
    #         if user.has_perm('products.change_product'):
    #             return True
    #         if user.has_perm('products.delete_product'):
    #             return True
    #         if user.has_perm('products.view_product'):
    #             return True
    #         return False
    #     return False
    