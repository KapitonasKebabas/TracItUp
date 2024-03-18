from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserMedecineListView.as_view(), name='user-medicine-list'),
    path('aproved/list/', views.AprovedMedecineListView.as_view(), name='aproved-medicine-list'),
    path('delete/<int:pk>/', views.UserMedecineDeleteView.as_view(), name='user-medicine-delete'),
    path('update/<int:pk>/', views.UserMedecineUpdateView.as_view(), name='user-medicine-update')
]
