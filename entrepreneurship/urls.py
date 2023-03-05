from django.urls import path
from .views import ParticipationCreateView , ParticipationListView, ParticipationDetailView, ParticipationUpdateView, ParticipationDeleteView #, MemberCreateView, MemberListView, MemberDetailView, MemberUpdateView, MemberDeleteView

urlpatterns = [
    path('participation-create/', ParticipationCreateView.as_view()),
    path('participation-list/', ParticipationListView.as_view()),
    path('participation-detail/<int:pk>/', ParticipationDetailView.as_view()),
    path('participation-update/<int:pk>/', ParticipationUpdateView.as_view()),
    path('participation-delete/<int:pk>/', ParticipationDeleteView.as_view()),

    # path('member-create/', MemberCreateView.as_view()),
    # path('member-list/', MemberListView.as_view()),
    # path('member-detail/<int:pk>/', MemberDetailView.as_view()),
    # path('member-update/<int:pk>/', MemberUpdateView.as_view()),
    # path('member-delete/<int:pk>/', MemberDeleteView.as_view()),

]