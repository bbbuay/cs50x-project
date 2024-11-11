from django.urls import path
from .views import RegisterUserView, UserProfileView, FavoriteGuidanceView, login_view, register_view, profile_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('profile', profile_view, name='profile'),

    # API endpoints
    path('api/register/', RegisterUserView.as_view(), name='register_user'),
    path('api/profile/', UserProfileView.as_view(), name='get_user_profile'),
    path('api/user/favorite-guidances/', FavoriteGuidanceView.as_view(), name='get-favorite-guidances')
]