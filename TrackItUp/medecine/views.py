from django.shortcuts import render

from rest_framework             import generics, status
from rest_framework.response            import Response

from .models        import AprovedMedecine, UserMedecine, OrderStatus, Orders
from .serializers   import UserMedecineSerializer, AprovedMedecineSerializer, SharedMedecineSerializer, OrderStatusesSerializer, OrdersSerializer

from authorization.mixins import UserGetPostPermissionMixin

from django.utils import timezone



# Create your views here.
class AprovedMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = AprovedMedecineSerializer
    queryset = AprovedMedecine.objects.filter(is_aproved=True)

class UserMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = UserMedecineSerializer

    def get_queryset(self):
        return UserMedecine.objects.filter(user=self.request.user)
    
class SharedMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = SharedMedecineSerializer

    def get_queryset(self):
        return UserMedecine.objects.exclude(user=self.request.user).filter(is_shared=True, shared_qty__gt=0, medecine__is_prescription=False, exp_date__gt=timezone.now().date())

class OrdersListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.filter(user_buyer=self.request.user)

class OrdersCreateView(UserGetPostPermissionMixin, generics.CreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def create(self, request, *args, **kwargs):
        json_payload = request.data
        json_payload['user_buyer_id'] = request.user.pk

        serializer = self.get_serializer(data=json_payload)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersUpdateView(UserGetPostPermissionMixin, generics.UpdateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    lookup_field = 'pk'

class OrderStatusesListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = OrderStatusesSerializer

    def get_queryset(self):
        return OrderStatus.objects.all()

class UserMedecineDeleteView(UserGetPostPermissionMixin, generics.DestroyAPIView):
    serializer_class = UserMedecineSerializer
    queryset = UserMedecine.objects.all()
    lookup_field='pk'

class UserMedecineUpdateView(UserGetPostPermissionMixin, generics.UpdateAPIView):
    serializer_class = UserMedecineSerializer
    queryset = UserMedecine.objects.all()
    lookup_field = 'pk'

class UserMedecineCreateView(UserGetPostPermissionMixin, generics.CreateAPIView):
    serializer_class = UserMedecineSerializer
    queryset = UserMedecine.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)