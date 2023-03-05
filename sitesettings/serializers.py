from rest_framework import serializers
from .models import SMTPSetting, Notification

class SmtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMTPSetting
        fields = ['id','email_host_user','email_host_password','email_port']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"