from rest_framework import generics
from .serializers import RegisterUserSerializer, UserSerializer, FavoriteGuidanceSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FavoriteGuidanceView(generics.ListAPIView):
    serializer_class = FavoriteGuidanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.favorite_guidances.all()
    
class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
    

# render pages
def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

def profile_view(request):
    return render(request, "profile.html")