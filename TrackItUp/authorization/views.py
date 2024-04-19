from django.shortcuts       import render
from django.contrib.auth    import logout
from django.shortcuts       import get_object_or_404

from cprofile.models import CustomUser as User

from rest_framework_simplejwt.views     import TokenViewBase, TokenObtainPairView
from rest_framework_simplejwt.tokens    import RefreshToken
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework.authtoken.models    import Token


from TrackItUp import settings

from .decrypt       import decrypt_password
from .mixins        import UserGetPostPermissionMixin, StaffEditorPermissionMixin, NoPermissionMixin
from .serializers   import UserRegistrationSerializer, UserProfileSerializer

import json

# Create your views here.
class CustomObtainAuthToken(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        """
        config = settings.config

        encrypted_password = request.data.get('password', None)

        key = config['PASS_KEY'] # Replace with your encryption key

        if encrypted_password:
            request.data._mutable = True
            decrypted_password = decrypt_password(encrypted_password, key)
            request.data['password'] = decrypted_password
        return super().post(request, *args, **kwargs)
        """
        return super().post(request, *args, **kwargs)
    
class UserLogoutView(TokenViewBase, UserGetPostPermissionMixin):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        try:
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)
    
class UserCheckTokenView(generics.GenericAPIView, UserGetPostPermissionMixin):
    def post(self, request):
        username = request.data.get('username')
        print(username)
        user = User.objects.filter(username=username).first()
        token = request.auth
        print(token)
        token_user = Token.objects.filter(key=token).first().user 

        if token_user == user:
            return Response({'response': 'success'})
        
        return Response({'response': 'Invalid token or username'}, status=400)
    
class UserRegistrationView(NoPermissionMixin, generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """config = settings.config
        encrypted_password = request.data.get('password', None)
        key = config['PASS_KEY']

        mutable_data = request.data.copy()

        #print(encrypted_password)
        if encrypted_password:
            decrypted_password = decrypt_password(encrypted_password, key)
            mutable_data['password'] = decrypted_password
        else:
            mutable_data['password'] = ""
        #print(encrypted_password)
        serializer = self.get_serializer(data=mutable_data)"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'response': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveAPIView, UserGetPostPermissionMixin):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        return obj
