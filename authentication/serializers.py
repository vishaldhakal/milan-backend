from rest_framework import serializers
from .models import User, UserSession
from django.contrib.auth import authenticate
from django.db.models import Q 
from django.contrib import auth
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import AuthenticationFailed, ValidationError




class RegisterUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    #confirm_password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [ 'email', 'username', 'password','contact_number']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password')
        contact_number = attrs.get('contact_number')
        # confirm_password = attrs.pop('confirm_password')
        # if password != confirm_password:
        #     raise serializers.ValidationError('passwords should be same')
        if not username.isalnum():
            raise serializers.ValidationError({'username': 'The username should only contain only alphanumeric value'})
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','full_name','username','email','contact_number','image','slogan','slogan_image']

class EmailVerificationSerializers(serializers.ModelSerializer):
    tokens = serializers.CharField(max_length=555, help_text="Enter same email as you have provided during regristrations")

    class Meta:
        model = User
        fields = ['tokens']


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        """override meta class"""
        model = User
        fields = ('old_password', 'new_password')

    def validate_new_password(self, value):
        validate_password(value)
        return value


class UserLoginSerializer(TokenObtainPairSerializer):
    """
    For login user
    """
    default_error_messages = {
        'no_active_account': 'Username or Password does not matched.'
    }

    @classmethod
    def get_token(cls,user):
        '''pass'''
        token = super().get_token(user)

        obj=User.objects.get(id=user.id)
        token['username'] = user.username
        token['email'] = obj.email
        token['is_superuser'] = obj.is_superuser

        return token

    def validate(self, attrs):
        '''pass'''
        username = attrs.get('username')
        password = attrs.get('password')
        try:
            us = User.objects.get(Q(email=attrs.get("username"))| Q(username=attrs.get("username")))
            print(us)
            username = us.username
        except Exception as e:
            print(e)
            pass
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('Invalid Crendential, Try again')

        refresh = self.get_token(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return {
            'access': access_token,
            'refresh': refresh_token,
        }


class PasswordResetSerializers(serializers.Serializer):
    """serializer for password reset request. It validates email."""
    email = serializers.EmailField(max_length=256, min_length=2)

    class Meta:
        """override meta class"""
        fields = ['email']

class NewPasswordSerializers(serializers.Serializer):
    password = serializers.CharField(
        max_length=68, min_length=2, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        """override meta class"""
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        """override validate method"""
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id','ip','device_type','browser','location']

