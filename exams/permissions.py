# exams/permissions.py
from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow teachers to edit and delete exams and questions,
    but only allow read access to others.
    """

    def has_permission(self, request, view):
        
        # Allow read access to authenticated
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated:
            return True
        
        # Check if the user is a teacher
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Teacher_Group').exists()
