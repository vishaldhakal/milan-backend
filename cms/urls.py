from django.urls import path
from .views import ContactMeListView, ContactMeCreateView, ContactMeDetailView, ContactMeUpdateView, ContactMeDeleteView, AboutMeListView, AboutMeCreateView, AboutMeDetailView, AboutMeUpdateView, AboutMeDeleteView, FindUsCreateView, FindUsListView, FindUsDetailView, FindUsUpdateView, FindUsDeleteView, ImageListView, ImageUpdateView, LogoImageListView, LogoImageUpdateView, VideosListView, VideosCreateView, VideosDetailView, VideosUpdateView, VideosDeleteView, PublishVideosListView,QuestionCreateView, QuestionListView, QuestionDetailView, QuestionUpdateView, QuestionDeleteView, AnswerCreateView, AnswerListView, AnswerDetailView, AnswerUpdateView, AnswerDeleteView, UserDetailListView

urlpatterns = [
    path('aboutus-list/', AboutMeListView.as_view()),
    path('aboutus-create/', AboutMeCreateView.as_view()),
    path('aboutus-detail/<int:pk>/', AboutMeDetailView.as_view()),
    path('aboutus-update/<int:pk>/', AboutMeUpdateView.as_view()),
    path('aboutus-delete/<int:pk>/', AboutMeDeleteView.as_view()),

    path('contact-me-list/', ContactMeListView.as_view()),
    path('contact-me-create/', ContactMeCreateView.as_view()),
    path('contact-me-detail/<int:pk>/', ContactMeDetailView.as_view()),
    path('contact-me-update/<int:pk>/', ContactMeUpdateView.as_view()),
    path('contact-me-delete/<int:pk>/', ContactMeDeleteView.as_view()),

    path('find-us-create/', FindUsCreateView.as_view()),
    path('find-us-list/', FindUsListView.as_view()),
    path('find-us-detail/<int:pk>/', FindUsDetailView.as_view()),
    path('find-us-update/<int:pk>/', FindUsUpdateView.as_view()),
    path('find-us-delete/<int:pk>/', FindUsDeleteView.as_view()),

    path('image-list/', ImageListView.as_view()),
    path('image-update/<int:pk>/', ImageUpdateView.as_view()),

    path('logo-image-list/', LogoImageListView.as_view()),
    path('logo-image-update/<int:pk>/', LogoImageUpdateView.as_view()),

    path('video-create/', VideosCreateView.as_view()),
    path('video-list/', VideosListView.as_view()),
    path('video-detail/<int:pk>/', VideosDetailView.as_view()),
    path('video-update/<int:pk>/', VideosUpdateView.as_view()),
    path('video-delete/<int:pk>/', VideosDeleteView.as_view()),
    path('publish-video-list/', PublishVideosListView.as_view()),

    path('question-create/', QuestionCreateView.as_view()),
    path('question-list/', QuestionListView.as_view()),
    path('question-detail/<int:pk>/', QuestionDetailView.as_view()),
    path('question-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('question-delete/<int:pk>/', QuestionDeleteView.as_view()),

    path('answer-create/', AnswerCreateView.as_view()),
    path('answer-list/', AnswerListView.as_view()),
    path('answer-detail/<int:pk>/', AnswerDetailView.as_view()),
    path('answer-update/<int:pk>/', AnswerUpdateView.as_view()),
    path('answer-delete/<int:pk>/', AnswerDeleteView.as_view()),

    path('user-detail-list/', UserDetailListView.as_view()),

    
    

]