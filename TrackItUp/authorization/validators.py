from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from cprofile.models import CustomUser as User


unique_user = UniqueValidator(queryset=User.objects.all(), lookup='iexact')