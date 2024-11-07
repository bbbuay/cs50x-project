from rest_framework import generics
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
