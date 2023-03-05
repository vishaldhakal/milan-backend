from rest_framework import generics
from .models import SMTPSetting
from .serializers import SmtpSerializer
from .models import Notification



class SmtpDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Smtp details update and delete"""
    serializer_class = SmtpSerializer
    queryset = SMTPSetting.objects.all()
    lookup_field = 'id'


class SmtpView(generics.ListCreateAPIView):
    """Smtp list and create"""
    serializer_class = SmtpSerializer
    queryset = SMTPSetting.objects.all()



def add_notification(request,model_name,obj_name):
    if request.method=="POST":
        m_name=model_name.__name__
        Notification.objects.create(status='added',obj_name=obj_name,model_name=m_name)
        return
    
