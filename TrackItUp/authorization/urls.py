from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.CustomObtainAuthToken.as_view(), name='user-obtainauth'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('delete/', views.UserLogoutView.as_view(), name='user-logout'),
    path('checkauth/', views.UserCheckTokenView.as_view(), name='user-checktoken')
]
