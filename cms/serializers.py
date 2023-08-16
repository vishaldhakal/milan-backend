from rest_framework import serializers
from .models import AboutMe, ContactMe, SocialMediaLink, LogoImage, Image, Videos, Question, Answer, UserDetail,SurveyConfig,Survey

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['id','content','image','created_at','updated_at']


class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMe
        fields = ['id','name','message','email','subject','phone_number','address','created_at','updated_at']

class FindUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ['id','facebook','twitter','youtube','linkedin','instagram','tiktok']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image1','image2','image3']

class LogoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoImage
        fields = ['id','image']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id','title','live_link','is_publish','created_at']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id','answer','first_name','last_name','email','phone_number','address']

class UserDetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id','answer','first_name','last_name','email','phone_number','address']

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','question','answer']

class AnswerListSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    user_answer = UserDetailListSerializer(read_only=True,many=True)
    class Meta:
        model = Answer
        fields = ['id','question','answer','user_answer']


class SurveyConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyConfig
        fields = '__all__'    

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'    


        



