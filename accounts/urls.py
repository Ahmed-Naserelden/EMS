from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin, name='signinp'),
    path('signout/', views.signout, name='signoutp'),
    
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
    
    path('teachers/<int:pk>', views.TeacherDetail.as_view(), name='student-list'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='teacher-list'),
    
    path('teacherprofile/<int:pk>/', views.teacherprofile, name='teacherprofile'),
    path('studentprofile/<int:pk>/', views.studentprofile, name='studentprofile'),
    
    path('addteacher/', views.addteacher, name='add-teacher'),
    path('', views.getAllInSchool, name='all-in-school'),

    # token authentications
    path('api-token-auth/', obtain_auth_token),
    path('myprofile/', views.myprofile, name='myprofile'),
    
]
