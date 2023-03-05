from django.db import models

class Participation(models.Model):
    name_of_business = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    business_model = models.FileField(upload_to='participation/files/',max_length=150)
    estimated_cost = models.FileField(upload_to='participation/files/',max_length=150)
    estimated_timeframe = models.FileField(upload_to='participation/files/',max_length=150)
    estimated_roi = models.FileField(upload_to='participation/files/',max_length=150)
    project_detail = models.FileField(upload_to='participation/files/',max_length=150,blank=True,null=True)
    noteworthy_impact = models.FileField(upload_to='participation/files/',max_length=150,blank=True,null=True)
    noteworthy_mentions = models.FileField(upload_to='participation/files/',max_length=150,blank=True,null=True)
    member = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# class Member(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     participation = models.ForeignKey(Participation,on_delete=models.CASCADE,related_name='participation_member')

#     def __str__(self):
#         return self.first_name
