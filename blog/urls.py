from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, PublishedPostListView

urlpatterns = [
    path('post-list/', PostListView.as_view(),name='posts'),
    path('published-post-list/', PublishedPostListView.as_view()),
    path('post-create/', PostCreateView.as_view(),name='post-create'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view()),
    path('post-update/<slug:slug>/', PostUpdateView.as_view(),name='post-update'),
    path('post-delete/<slug:slug>/', PostDeleteView.as_view()),
]
