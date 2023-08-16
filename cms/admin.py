from django.contrib import admin
from .models import AboutMe, ContactMe, SocialMediaLink, LogoImage, Image, Videos, Question, Answer, UserDetail,Survey,SurveyConfig
from solo.admin import SingletonModelAdmin

admin.site.register(AboutMe)
admin.site.register(ContactMe)
admin.site.register(SocialMediaLink)
admin.site.register(LogoImage)
admin.site.register(Image)
admin.site.register(Videos)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserDetail)
admin.site.register(SurveyConfig,SingletonModelAdmin)
admin.site.register(Survey)



