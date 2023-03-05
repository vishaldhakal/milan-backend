from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError



class User(AbstractUser):
    '''user model'''
    full_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    username = models.CharField(max_length=255,unique=True)
    contact_number = models.CharField(max_length=15,unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='images/',validators=[FileExtensionValidator(['png','jpg','jpeg'])],null=True,blank=True)
    is_email_verified = models.BooleanField(default=False)
    code = models.CharField(max_length=500,null=True,blank=True)
    code_created = models.DateTimeField(blank=True, null=True)
    slogan = models.TextField(max_length=1000,null=True,blank=True)
    slogan_image = models.ImageField(upload_to='slogan/images',null=True,blank=True)

    REQUIRED_FIELDS = ['email',]

    def save(self, *args, **kwargs):
        if not self.pk and User.objects.exists():
            raise ValidationError('user can be created only once')
        return super(User, self).save(*args,**kwargs)

    def delete(self):
        raise PermissionError("delete action is not allowed")
        

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class UserSession(models.Model):
    ip = models.CharField(max_length=16, null=True, blank=True)
    device_type = models.CharField(max_length=255, null=True, blank=True)
    browser = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return f'{self.ip}'

