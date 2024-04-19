from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserMedecineListView.as_view(), name='user-medicine-list'),
    path('aproved/list/', views.AprovedMedecineListView.as_view(), name='aproved-medicine-list'),
    path('delete/<int:pk>/', views.UserMedecineDeleteView.as_view(), name='user-medicine-delete'),
    path('update/<int:pk>/', views.UserMedecineUpdateView.as_view(), name='user-medicine-update'),
    path('add/', views.UserMedecineCreateView.as_view(), name='user-medicine-add'),
    path('shared/list/', views.SharedMedecineListView.as_view(), name='shared-medicine-add'),
    path('order/list/', views.OrdersListView.as_view(), name='order-list'),
    path('order/add/', views.OrdersCreateView.as_view(), name='order-add'),
    path('order/update/<int:pk>/', views.OrdersUpdateView.as_view(), name='order-update'),
    path('order/statuses/', views.OrderStatusesListView.as_view(), name='order-statuses'),
]
