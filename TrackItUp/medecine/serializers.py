from rest_framework import serializers 
from cprofile.models import CustomUser as User
from .models import UserMedecine, AprovedMedecine, Orders, OrderStatus

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

class SharedMedecineSerializer(serializers.ModelSerializer):
    user_pk                 = serializers.CharField(source='user.pk', read_only=True)
    user_name               = serializers.CharField(source='user.username', read_only=True)
    medecine_name           = serializers.CharField(source='medecine.name', read_only=True)
    medecine_description    = serializers.CharField(source='medecine.description', read_only=True) 

    class Meta:
        model = UserMedecine
        fields = [
            'pk',
            'medecine',
            'medecine_name',
            'medecine_description',
            'shared_qty',
            'shared_reserved_qty',
            'user_pk',
            'user_name'
        ]


class AprovedMedecineSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

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
    
    def get_photo(self, obj):
        # Open and read the image file
        print(obj.photo)
        with open(obj.photo.path, 'rb') as f:
            image_data = f.read()

        # Encode the image data as base64
        import base64
        return base64.b64encode(image_data).decode('utf-8')
    

class OrderStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = [
            'pk',
            'name',
            'helptext'
        ]

class OrdersSerializer(serializers.ModelSerializer):
    status                = serializers.PrimaryKeyRelatedField(queryset=OrderStatus.objects.all())
    aproved_medecine      = serializers.CharField(source='user_medicine.medecine.pk', read_only=True)
    medecine              = serializers.CharField(source='user_medicine.pk', read_only=True)
    medecine_name         = serializers.CharField(source='user_medicine.medecine.name', read_only=True)
    status_name           = serializers.CharField(source='status.name', read_only=True)
    status_helptext       = serializers.CharField(source='status.helptext', read_only=True) 
    user_seller_pk        = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user_seller')
    user_seller_username      = serializers.CharField(source='user_seller.username', read_only=True)
    user_buyer_pk         = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user_buyer')
    user_buyer_username       = serializers.CharField(source='user_buyer.username', read_only=True)
    user_medicine_pk      = serializers.PrimaryKeyRelatedField(queryset=UserMedecine.objects.all(), source='user_medicine')

    class Meta:
        model = Orders
        fields = [
            'pk',
            'aproved_medecine',
            'medecine',
            'medecine_name',
            'user_seller_pk',
            'user_seller_username',
            'user_buyer_pk',
            'user_buyer_username',
            'user_medicine_pk',
            'qty',
            'status',
            'status_name',
            'status_helptext'
        ]

    def update(self, instance, validated_data):
        status = validated_data.get('status')
        qty = validated_data.get('qty')
        medecine = validated_data.get('user_medicine')

        if status.pk == 1: #Atsaukta
            medecine.shared_reserved_qty -= qty
            medecine.shared_qty += qty
            pass
        elif status.pk == 2: #Baigta
            medecine.shared_reserved_qty -= qty
            pass
        elif status.pk == 3: #Vykdoma
            medecine.shared_reserved_qty += qty
            medecine.shared_qty -= qty
            pass
        
        medecine.save()

        instance = super().update(instance, validated_data)

        return instance
    
    def create(self, validated_data):
        qty = validated_data.get('qty')
        medecine = validated_data.get('user_medicine')

        medecine.shared_reserved_qty += qty
        medecine.shared_qty -= qty
        
        medecine.save()
        
        return Orders.objects.create(**validated_data)