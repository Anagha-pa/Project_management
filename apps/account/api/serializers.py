from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from ..models import UserData
from ..models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid email or password.")
            
            
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")

            data['user'] = user
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")
        return data

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "username", "password", "mobile"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'], username=validated_data['username'], password=validated_data['password'], mobile=validated_data['mobile'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    