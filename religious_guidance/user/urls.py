from django.urls import path
from .views import RegisterUserView, UserView, FavoriteGuidanceView, UpdateProfileView, login_view, register_view, profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),

    # API endpoints
    path('api/register/', RegisterUserView.as_view(), name='register_user'),
    path('api/user/', UserView.as_view(), name='get_user'),
    path('api/profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('api/user/favorite-guidances/', FavoriteGuidanceView.as_view(), name='get-favorite-guidances'),
]