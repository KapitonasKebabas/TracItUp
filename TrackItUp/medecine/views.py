from django.shortcuts import render

from rest_framework             import generics

from .models        import AprovedMedecine, UserMedecine
from .serializers   import UserMedecineSerializer, AprovedMedecineSerializer

from authorization.mixins import UserGetPostPermissionMixin

# Create your views here.
class AprovedMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = AprovedMedecineSerializer
    queryset = AprovedMedecine.objects.filter(is_aproved=True)

class UserMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = UserMedecineSerializer

    def get_queryset(self):
        return UserMedecine.objects.filter(user=self.request.user)
    
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