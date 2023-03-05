from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .paginations import BlogAdminPagination
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class PostListView(generics.ListAPIView):
    '''blog list for post'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = BlogAdminPagination
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['title','author']
    ordering_fields = ['title','author','created_at']
    

class PublishedPostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    pagination_class = BlogAdminPagination
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['title','author']
    ordering_fields = ['title','author']

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        print(request.data)
        print(self.request.user)
        
        post_serializer = PostSerializer(data=request.data)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
