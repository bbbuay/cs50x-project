from rest_framework import generics
from .serializers import RegisterUserSerializer, UserProfileSerializer, FavoriteGuidanceSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FavoriteGuidanceView(generics.ListAPIView):
    serializer_class = FavoriteGuidanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.favorite_guidances.all()
    

# render pages
def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

def profile_view(request):
    return render(request, "profile.html")