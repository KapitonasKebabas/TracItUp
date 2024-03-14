from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomObtainAuthToken.as_view(), name='user-obtainauth')
    #path('auth/delete/', views.UserLogoutView.as_view(), name='user-logout'),
    #path('auth/checkauth/', views.UserCheckTokenView.as_view(), name='user-checktoken'),
    #path('auth/register/', views.UserRegistrationView.as_view(), name='user-registration'),
]
