from django.shortcuts import render
from rest_framework import generics, status
from .models import ContactMe, AboutMe, SocialMediaLink, LogoImage, Image, Videos, Question, Answer, UserDetail
from rest_framework.response import Response
from .serializers import ContactMeSerializer, AboutMeSerializer, LogoImageSerializer, ImageSerializer, VideoSerializer, FindUsSerializer,  QuestionSerializer, AnswerCreateSerializer, AnswerListSerializer,UserDetailSerializer, UserDetailListSerializer
from blog.paginations import BlogAdminPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from blog.paginations import BlogAdminPagination
from django.contrib import messages
from sitesettings.views import add_notification
from rest_framework.exceptions import APIException
from authentication.models import User
from django.core.mail import send_mail
from authentication.utils import Util


class AboutMeListView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class AboutMeCreateView(generics.CreateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):

        serializer = AboutMeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutMeDetailView(generics.RetrieveAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class AboutMeUpdateView(generics.UpdateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class AboutMeDeleteView(generics.DestroyAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class ContactMeListView(generics.ListAPIView):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
    pagination_class = BlogAdminPagination
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['name','email']
    ordering_fields = ['name','created_at']


class ContactMeCreateView(generics.CreateAPIView):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer

    def post(self, request, *args, **kwargs):
        contact_serializer = ContactMeSerializer(data=request.data)
        if contact_serializer.is_valid():
            contact_me = contact_serializer.save()
            user_email = contact_me.email
            user_message = contact_me.message
            user_name = contact_me.name
            user_subject = contact_me.subject
            user_phone = contact_me.phone_number
            admin_email = User.objects.get(is_superuser = True).email
            print(admin_email)
            data = {
                'name':user_name,
                'user_email':user_email,
                'user_phone':user_phone,
                'subject':user_subject,
                'user_message':user_message,
                'email_subject':'Someone tried to reach you from milan portfolio site',
                'email_receiver': admin_email
            }
            Util.send_mail_admin(data)

            user_data = {
                'name': user_name,
                'email_subject': 'Thanks for reaching out to us',
                'email_body':  'Hi,\n\nThank you for contacting me. I will reach back to you as soon as possible. Take care\n\nRegards,\nMJK',
                'email_receiver': user_email
            }
            Util.send_mail_register(user_data)

            return Response(contact_serializer.data, status = status.HTTP_201_CREATED)
        return Response(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactMeDetailView(generics.RetrieveAPIView):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class ContactMeUpdateView(generics.UpdateAPIView):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class ContactMeDeleteView(generics.DestroyAPIView):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class FindUsCreateView(generics.CreateAPIView):
    queryset = SocialMediaLink.objects.all()
    serializer_class = FindUsSerializer
    permission_classes = [IsAdminUser]


class FindUsListView(generics.ListAPIView):
    queryset = SocialMediaLink.objects.all()
    serializer_class = FindUsSerializer


class FindUsDetailView(generics.RetrieveAPIView):
    queryset = SocialMediaLink.objects.all()
    serializer_class = FindUsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class FindUsUpdateView(generics.UpdateAPIView):
    queryset = SocialMediaLink.objects.all()
    serializer_class = FindUsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class FindUsDeleteView(generics.DestroyAPIView):
    queryset = SocialMediaLink.objects.all()
    serializer_class = FindUsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageUpdateView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'pk'

class LogoImageListView(generics.ListAPIView):
    queryset = LogoImage.objects.all()
    serializer_class = LogoImageSerializer


class LogoImageUpdateView(generics.UpdateAPIView):
    queryset = LogoImage.objects.all()
    serializer_class = LogoImageSerializer
    lookup_field = 'pk'



class VideosListView(generics.ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    pagination_class = BlogAdminPagination
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['title']
    ordering_fields = ['title','created_at']
    filterset_fields = {
        'title':['exact'],
    }

class PublishVideosListView(generics.ListAPIView):
    queryset = Videos.objects.filter(is_publish=True)
    serializer_class = VideoSerializer
    pagination_class = BlogAdminPagination
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['title']
    ordering_fields = ['created_at']
    filterset_fields = {
        'title':['exact'],
    }


class VideosCreateView(generics.CreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):

        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideosDetailView(generics.RetrieveAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'pk'


class VideosUpdateView(generics.UpdateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'pk'


class VideosDeleteView(generics.DestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'pk'


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):

        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    #filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer

    def create_user(self,answer_info):
        try:
            data1 = {}
            u = self.request.data['user']

            data1['first_name'] = u['first_name']
            data1['last_name'] = u['last_name']
            data1['email'] = u['email']
            data1['phone_number'] = u['phone_number']
            data1['address'] = u['address']
            data1['answer'] = int(answer_info)
            serializer = UserDetailSerializer(data=data1)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            admin_email = User.objects.filter(is_superuser=True).first().email
            user_question = user.answer.question
            user_answer = user.answer
            first_name = user.first_name
            last_name = user.last_name
            user_email = user.email
            user_phone_number = user.phone_number
            user_address = user.address

            data = {
                'email_receiver':admin_email,
                'user_question':user_question,
                'user_answer':user_answer,
                'first_name':first_name,
                'last_name':last_name,
                'user_email':user_email,
                'user_phone_number':user_phone_number,
                'user_address':user_address,
                'email_subject':'An individual has submitted a response to the Giveaway Form'
            }
            Util.send_mail_admin_for_answer(data)
        except Exception as e:
            print(e)
            raise APIException("Cant't add answer")
        return 

    def send_mail_user_for_answer(self, user_email):
        try:
            email_subject = "We have received your answer"
            email_body = "Hi,\n\nThank you for submitting your answer. We will keep in touch. Take care\n\nRegards,\nMJK"
            data = {
                'email_receiver':user_email,
                'email_subject':email_subject,
                'email_body':email_body
            }
            Util.send_mail_register(data)
        except Exception as e:
            print(e)
            raise APIException("Can't send email to user")



    def post(self, request, *args, **kwargs):

        serializer = AnswerCreateSerializer(data=request.data['answer'])

        if serializer.is_valid():
            
            serializer.save()
            self.create_user(serializer.data['id'])
            self.send_mail_user_for_answer(request.data['user']['email'])
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerListView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    pagination_class = BlogAdminPagination
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['user_answer__name','user_answer__email']
    ordering_fields = ['user_answer__name']

class AnswerDetailView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    lookup_field = 'pk'


class AnswerUpdateView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    lookup_field = 'pk'


class AnswerDeleteView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    lookup_field = 'pk'


class UserDetailListView(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailListSerializer



    






