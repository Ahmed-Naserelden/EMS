# exams/permissions.py
from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        # Allow read access to authenticated
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated:
            return True
        
        # Check if the user is a teacher
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Teacher_Group').exists()

class IsPrinciple(permissions.BasePermission):

    def has_permission(self, request, view):
        
        # # Allow read access to authenticated
        # if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated:
        #     return True
        
        # Check if the user is a Principle
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Principle').exists()


class IsPrincipleOrSelf(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        return request.user and request.user.is_authenticated and (request.user.groups.filter(name='Principle').exists() or obj.user == request.user)

    