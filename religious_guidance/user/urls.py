from django.urls import path
from .views import RegisterUserView, UserProfileView, FavoriteGuidanceView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('profile/', UserProfileView.as_view(), name='get_user_profile'),
    path('user/favorite-guidances/', FavoriteGuidanceView.as_view(), name='get-favorite-guidances')
]