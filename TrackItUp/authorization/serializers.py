from rest_framework import serializers 
from rest_framework.validators import UniqueValidator

from cprofile.models import CustomUser as User
from django.contrib.auth.models                 import Group
from django.contrib.auth.password_validation    import validate_password as django_validate_password

from . import validators

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='This username is already in use.'),
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='This email address is already in use.'),
        ]
    )
    password = serializers.CharField(
        validators=[
            django_validate_password,
        ]
    )
    
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username    = validated_data['username'],
            first_name  = validated_data['first_name'],
            last_name   = validated_data['last_name'],
            email       = validated_data['email'],
            password    = validated_data['password']
        )

        users_group = Group.objects.get(name='Users')
        if(users_group):
            user.groups.add(users_group)

        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'is_staff'
            ]