from django.urls import path
from .views import RegisterUserView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('profile/', UserProfileView.as_view(), name='get_user_profile'),
]