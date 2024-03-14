from django.shortcuts import render
from rest_framework.authtoken.views     import ObtainAuthToken
from TrackItUp import settings
from .decrypt       import decrypt_password

# Create your views here.
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        config = settings.config

        encrypted_password = request.data.get('password', None)
        key = config['PASS_KEY'] # Replace with your encryption key

        if encrypted_password:
            request.data._mutable = True
            decrypted_password = decrypt_password(encrypted_password, key)
            request.data['password'] = decrypted_password

        return super().post(request, *args, **kwargs)