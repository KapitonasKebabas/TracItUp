from django.shortcuts import render

from rest_framework             import generics

from .models        import AprovedMedecine, UserMedecine
from .serializers   import UserMedecineSerializer

from authorization.mixins import UserGetPostPermissionMixin

# Create your views here.
class AprovedMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = AprovedMedecine
    queryset = AprovedMedecine.objects.filter(is_aproved=True)

class UserMedecineListView(UserGetPostPermissionMixin, generics.ListAPIView):
    serializer_class = UserMedecineSerializer

    def get_queryset(self):
        return UserMedecine.objects.filter(user=self.request.user)