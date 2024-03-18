from rest_framework import serializers 

from .models import UserMedecine, AprovedMedecine

class UserMedecineSerializer(serializers.ModelSerializer):
    medecine                = serializers.PrimaryKeyRelatedField(queryset=AprovedMedecine.objects.all())
    medecine_name           = serializers.CharField(source='medecine.name', read_only=True)
    medecine_description    = serializers.CharField(source='medecine.description', read_only=True) 
    medecine_is_prescription= serializers.BooleanField(source='medecine.is_prescription', read_only=True)

    class Meta:
        model = UserMedecine
        fields = [
            'pk',
            'medecine',
            'medecine_name',
            'medecine_description',
            'medecine_is_prescription',
            'qty',
            'exp_date',
            'is_shared',
            'shared_qty',
        ]

class AprovedMedecineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AprovedMedecine
        fields = [
            'pk',
            'name',
            'description',
            'is_prescription',
            'photo',
            'is_aproved'
        ]