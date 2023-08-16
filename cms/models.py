from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from authentication.models import User 
from solo.models import SingletonModel

class AboutMe(models.Model):
    content = RichTextField(config_name='awesome_ckeditor')
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:25]

    def save(self, *args, **kwargs):
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError('about us can be created only once')
        return super(AboutMe, self).save(*args,**kwargs)

class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class SocialMediaLink(models.Model):
    facebook = models.URLField(max_length=200, blank=True, null= True)
    twitter = models.URLField(max_length=200, blank=True, null= True)
    youtube = models.URLField(max_length=200, blank=True, null= True)
    linkedin = models.URLField(max_length=200, blank=True, null= True)
    instagram = models.URLField(max_length = 200, blank=True, null = True)
    tiktok = models.URLField(max_length = 200, blank=True, null = True)

    def save(self,*args,**kwargs):
        if not self.pk and SocialMediaLink.objects.exists():
            raise ValidationError('create action not allowed')
        return super(SocialMediaLink, self).save(*args,**kwargs)

class LogoImage(models.Model):
    image = models.ImageField(upload_to='images/',validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True, null=True)

    def save(self,*args,**kwargs):
        if not self.pk and LogoImage.objects.exists():
            raise ValidationError('create action not allowed, only update existing one')
        return super(LogoImage, self).save(*args,**kwargs)


class Image(models.Model):
    image1 = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank =True, null=True)

    def save(self,*args,**kwargs):
        if not self.pk and Image.objects.exists():
            raise ValidationError('create action not allowed, only update existing one')
        return super(Image, self).save(*args,**kwargs)

class Videos(models.Model):
    title = models.CharField(max_length=300)
    live_link = models.URLField(null=True,blank=True)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        if not self.pk and Question.objects.exists():
            raise ValidationError('question can be created only once')
        return super(Question, self).save(*args,**kwargs)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True,blank=True)
    answer = models.TextField()

    def __str__(self):
        return self.answer[:15]

class UserDetail(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='user_answer',null=True,blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.first_name

class SurveyConfig(SingletonModel):
    title = models.CharField(max_length=400,blank=True)
    description = models.CharField(max_length=1000,blank=True)

    def __str__(self) -> str:
        return "Surver Title and Subtitle"
    
class Survey(models.Model):
    survey_title = models.CharField(max_length=400,blank=True)
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title