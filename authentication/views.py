from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserLoginSerializer, ChangePasswordSerializer, PasswordResetSerializers, RegisterUserSerializers, NewPasswordSerializers, EmailVerificationSerializers, UserSerializer, UserSessionSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import User, UserSession
import jwt
from django.urls import reverse
from .utils import Util
from rest_framework.views import APIView
from rest_framework import status
from django.utils.encoding import (DjangoUnicodeDecodeError, smart_bytes,
                                   smart_str)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import requests
from user_agents import parse
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializers
    permission_classes = (AllowAny, )

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = settings.FRONTEND_URL
        relative_link = reverse('verify_email')
        absurl = current_site + relative_link+"?token="+str(token)
        email_body = 'Hi there '+user.username+' Use this link to verify your email: \n'+ absurl
        data = {
            'email_subject': 'Email Confirmation',
            'email_body': email_body,
            'email_receiver': user.email,
            'email_user': user.username,
        }
        Util.send_mail_register(data)
        response = {
                    'success': 'mail has been sent successfully',
                    'user': user_data,
                    # 'token': str(token)
                }
        return Response(response, status=status.HTTP_201_CREATED)

class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializers

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,key= settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_email_verified:
                user.is_email_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifer:
            return Response({'error': 'Activation Expire'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifer:
            print(identifer)
            return Response({'error': 'Invalid Token'}, status = status.HTTP_400_BAD_REQUEST)



class LogInAPIView(TokenObtainPairView):
    """login user views"""
    serializer_class = UserLoginSerializer

class ChangePasswordView(APIView):
    """Change Password Views for User"""
    #queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        """pass"""
        return self.request.user

    def put(self, request, *args, **kwargs):
        """used to update password"""
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["wrong Password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'success': 'Successfully Changed User Password'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogOutView(APIView):
    """
    To log out a user this view is used
    """

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        """Blacklist the refresh token: extract token from the header
        during logout request user and refresh token is provided"""

        Refresh_token = request.data["refresh"]
        token = RefreshToken(Refresh_token)
        try:
            token.blacklist()
            response = {"message": "Successfully Logout !"}
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)
        except Exception:
            response = {"message": "Bad Token!"}
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status_code)


class PasswordResetView(GenericAPIView):
    """Views for password reset"""
    serializer_class = PasswordResetSerializers

    def post(self, request):
        """post method """
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        print(email)
        if User.objects.filter(email=email).exists():
            u = User.objects.get(email=email)
            uid64 = urlsafe_base64_encode(smart_bytes(u.id))
            tokens = PasswordResetTokenGenerator().make_token(u)
            # current_site = get_current_site(request= request).domain
            current_site = settings.FRONTEND_URL
            absurl = current_site + f'/password-reset/validate/{uid64}/{tokens}'
            email_body = 'Hi  '+u.username + '\n Someone (hopefully you) has requested a password reset for your Portfolio account. Follow the link below to set a new password: \n' + \
                absurl + '\nIf you do not wish to reset your password, disregard this email and no action will be taken.\nMilan Portfolio Team\n ' + current_site + '\n This link will be expired within 10 minutes.\n'
            data = {
                'email_subject': 'Password Reset',
                'email_body': email_body,
                'email_receiver': u.email
            }
            Util.send_mail_register(data)
            return Response({'success': 'We have send you a mail with instructions about changing your password.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email not registrered'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordTokenCheckView(GenericAPIView):
    """This views check token for validity"""

    serializer_class = RegisterUserSerializers

    def get(self, request, uidb64, token):
        """get method to get id"""
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, Please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'token validated'}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifer:
            return Response({'error': 'Token is not valid, Please send a new one'}, status=status.HTTP_401_UNAUTHORIZED)


class NewPasswordView(GenericAPIView):
    """Views to set new password of user"""
    serializer_class = NewPasswordSerializers

    def patch(self, request):
        """path new password"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': True, 'message': 'Password Reset completed'}, status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserPublicListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class UserDetailAuthView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserSessionDetailView(generics.RetrieveAPIView):
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer
    lookup_field = 'pk'

    def visitor_ip_address(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get(self,request,*args, **kwargs):
        location=(requests.get("https://geolocation-db.com/json/{ip}&position=true").json())
        print(location)
        ip = self.visitor_ip_address(request)

        
        data1 = {}
        a = self.request.META['HTTP_USER_AGENT']
        user_agent = parse(a)
        data1['ip']= ip
        data1['device_type']= user_agent.os.family
        data1['browser']= user_agent.browser.family
        data1['location']= location['country_name']
        u = UserSessionSerializer(data=data1)
        if u.is_valid():
            u.save()
            return Response(u.data)
        else:
            return Response(u.errors)


################ To Override Django admin dashboard for making login via email and password #######
# from django.contrib.auth.backends import ModelBackend

# class EmailOrUsernameModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         if '@' in username:
#             # Try to authenticate using the email
#             try:
#                 user = User.objects.get(email=username)
#                 if user.check_password(password):
#                     return user
#             except User.DoesNotExist:
#                 pass
#         else:
#             # Try to authenticate using the username
#             try:
#                 user = User.objects.get(username=username)
#                 if user.check_password(password):
#                     return user
#             except User.DoesNotExist:
#                 pass
#         return None
