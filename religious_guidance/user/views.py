from rest_framework import generics
from .serializers import RegisterUserSerializer, UserProfileSerializer
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
