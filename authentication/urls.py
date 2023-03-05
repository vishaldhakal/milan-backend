from django.urls import path
from .views import LogInAPIView, ChangePasswordView, LogOutView, PasswordResetView, ResetPasswordTokenCheckView, NewPasswordView, RegisterView, VerifyEmail, UserListView, UserUpdateView, UserDetailView, UserSessionDetailView, UserDetailAuthView, UserPublicListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns =[
    path('login/', LogInAPIView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name='verify_email'),
    path('logout/', LogOutView.as_view(), name='auth_logout'),
    path('change-password/<int:pk>/',
        ChangePasswordView.as_view(), name='auth_change_password'),

    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset/<uidb64>/<token>/', ResetPasswordTokenCheckView.as_view(),name = 'password_token_check'),
    path('password-reset-complete/', NewPasswordView.as_view()),

    path('user-list/', UserListView.as_view()),
    path('user-public-list/', UserPublicListView.as_view()),
    path('user-update/<int:pk>/', UserUpdateView.as_view()),
    path('user-auth-detail/<int:pk>/', UserDetailAuthView.as_view()),
    path('user-detail/<int:pk>/', UserDetailView.as_view()),

    path('user-session-detail/', UserSessionDetailView.as_view()),
]