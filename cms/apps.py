from django.apps import AppConfig
from django.db.models.signals import post_migrate


def generate_initial_obj(sender, **kwargs):
    from .models import AboutMe, LogoImage, Image, SocialMediaLink

    if not AboutMe.objects.exists():
        AboutMe.objects.create()
    if not LogoImage.objects.exists():
        LogoImage.objects.create()
    if not Image.objects.exists():
        Image.objects.create()
    if not SocialMediaLink.objects.exists():
        SocialMediaLink.objects.create()


class CmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cms'

    def ready(self):
        post_migrate.connect(generate_initial_obj, sender=self)
