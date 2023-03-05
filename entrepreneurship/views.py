from django.shortcuts import render
from rest_framework import generics, status
from .models import Participation
from rest_framework.response import Response
from .serializers import ParticipationCreateSerializer,ParticipationListSerializer
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAdminUser
from blog.paginations import BlogAdminPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


class ParticipationCreateView(generics.CreateAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationCreateSerializer

    # def member_create(self,part_info,data):
    #     try:
    #         data1 = {}
    #         for i in data:
    #             data1['first_name'] = i['first_name']
    #             data1['last_name'] = i['last_name']
    #             data1['participation'] = int(part_info)
    #             serializer = MemberSerializer(data=data1)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #     except Exception as e:
    #         print(e)
    #         raise APIException("Cant't add member info")
    #     return 

    def post(self, request):
        # print(request.data.keys())
        # print(request.data)
        serializer = ParticipationCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # self.member_create(serializer.data['id'],request.data.get('member'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)

        return Response(serializer.errors,status=status.HTTP_200_OK)

class ParticipationListView(generics.ListAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationListSerializer
    permission_classes = [IsAdminUser]
    pagination_class = BlogAdminPagination
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['name_of_business','email']
    ordering_fields = ['name_of_business','created_at']

class ParticipationDetailView(generics.RetrieveAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class ParticipationUpdateView(generics.UpdateAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class ParticipationDeleteView(generics.DestroyAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

# class MemberCreateView(generics.CreateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer

# class MemberListView(generics.ListAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#     permission_classes = [IsAdminUser]


# class MemberDetailView(generics.RetrieveAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#     permission_classes = [IsAdminUser]
#     lookup_field = 'pk'

# class MemberUpdateView(generics.UpdateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#     permission_classes = [IsAdminUser]
#     lookup_field = 'pk'

# class MemberDeleteView(generics.DestroyAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#     permission_classes = [IsAdminUser]
#     lookup_field = 'pk'
