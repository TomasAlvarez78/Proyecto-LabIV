from rest_framework import permissions

class DefaultPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        # Aca entran 2 tipos de usuarios
        # AuthenticatedUser & SuperUser

        allowed_methods = ['POST','GET','PUT','PATCH','DELETE']

        # print ("El request es:", request)
        # print ("Usuario :", request.user)

        if not request.user.is_authenticated:
            return False

        if request.method in allowed_methods:
            return True

class CarritoPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        # Aca entran 2 tipos de usuarios
        # AuthenticatedUser & SuperUser

        allowed_methods = ['POST','GET','PUT','PATCH','DELETE']

        # print ("El request es:", request)
        # print ("Usuario :", request.user)

        if request.user.is_authenticated and request.method in allowed_methods:
            return True

        return False
