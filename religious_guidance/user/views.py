from rest_framework import generics
from .serializers import RegisterUserSerializer, UserProfileSerializer, FavoriteGuidanceSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FavoriteGuidanceView(generics.ListAPIView):
    serializer_class = FavoriteGuidanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.favorite_guidances.all()