from django.contrib.auth import get_user_model, authenticate
from .models import DataConsolidado, Cobros, Recaudaciones
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'codigo_pago', 'token']  
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_token(self, user):
      
        try:
            token = Token.objects.get(user=user)
            return token.key
        except Token.DoesNotExist:
            return None

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        
       
        token, created = Token.objects.get_or_create(user=user)
        
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type':'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username=email,
            password=password 
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials", code='authentication')
        
        data['user'] = user
        return data

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})


class ClvDataSerializer (serializers.ModelSerializer):
    class Meta: 
        model = DataConsolidado
        fields = '__all__'

class ClvCobrosSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Cobros
        fields = '__all__'


class ClvRecaudacionesSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Recaudaciones
        fields = '__all__'

