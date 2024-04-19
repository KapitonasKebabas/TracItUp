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
    status_name           = serializers.CharField(source='status.name', read_only=True)
    status_helptext       = serializers.CharField(source='status.helptext', read_only=True) 
    user_seller_id        = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user_seller')
    user_seller_name      = serializers.CharField(source='user_seller.username', read_only=True)
    user_buyer_id         = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user_buyer')
    user_buyer_name       = serializers.CharField(source='user_buyer.username', read_only=True)
    user_medicine_pk      = serializers.PrimaryKeyRelatedField(queryset=UserMedecine.objects.all(), source='user_medicine')

    class Meta:
        model = Orders
        fields = [
            'pk',
            'user_seller_id',
            'user_seller_name',
            'user_buyer_id',
            'user_buyer_name',
            'user_medicine_pk',
            'qty',
            'status',
            'status_name',
            'status_helptext'
        ]