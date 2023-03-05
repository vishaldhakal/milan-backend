from rest_framework import serializers
from .models import Participation
from rest_framework.exceptions import ValidationError



class ParticipationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ['name_of_business','phone','email','business_model','estimated_cost','estimated_timeframe','estimated_roi','project_detail','noteworthy_impact','noteworthy_mentions','member']

class ParticipationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ['id','name_of_business','phone','email','business_model','estimated_cost','estimated_timeframe','estimated_roi','project_detail','noteworthy_impact','noteworthy_mentions','member','created_at']

# class ParticipationListSerializer(serializers.ModelSerializer):
#     participation_member = MemberSerializer(read_only=True, many=True)
#     class Meta:
#         model = Participation
#         fields = ['id','name_of_business','phone','email','business_model','estimated_cost','estimated_timeframe','estimated_roi','project_detail','noteworthy_impact','noteworthy_mentions','participation_member','created_at']

#     def validate_phone(self, value):
#         if len(str(value)) > 15:
#             raise ValidationError('Phone number should not be more than 15 digits')
#         return value

        