from rest_framework import serializers 

from .models import UserMedecine

class UserMedecineSerializer(serializers.ModelSerializer):
    medecine_name           = serializers.CharField(source='medecine.name', read_only=True)
    medecine_description    = serializers.CharField(source='medecine.description', read_only=True) 
    medecine_is_prescription= serializers.BooleanField(source='medecine.is_prescription', read_only=True)

    class Meta:
        model = UserMedecine
        fields = [
            'pk',
            'medecine_name',
            'medecine_description',
            'medecine_is_prescription',
            'qty',
            'exp_date',
            'is_shared',
            'shared_qty',
        ]