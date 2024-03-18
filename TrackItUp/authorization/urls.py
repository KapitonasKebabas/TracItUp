from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomObtainAuthToken.as_view(), name='user-obtainauth'),
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    #path('auth/delete/', views.UserLogoutView.as_view(), name='user-logout'),
    path('checkauth/', views.UserCheckTokenView.as_view(), name='user-checktoken')
]
