from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('exams/', include('exams.urls')),
        
    # token authentications
    path('api-token-auth/', obtain_auth_token),
]
