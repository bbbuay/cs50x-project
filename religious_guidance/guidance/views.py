from .models import Guidance
from .serializers import GuidanceSerializer
from random import randint
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RandomGuidanceDetail(generics.RetrieveAPIView):
    queryset = Guidance.objects.all()
    serializer_class = GuidanceSerializer

    def get_object(self) -> Guidance:
        # get the specific religion from query parameter
        religion = self.request.query_params.get('religion')

        queryset = self.get_queryset()

        # filter the queryset by religion (case-insensitive)
        if religion:
            queryset = queryset.filter(religion__iexact=religion)
        
        if not queryset:
            return Response({"message": "No guidance matching your search was found in the database."}, status=status.HTTP_404_NOT_FOUND)
        
        # get the random guidance
        random_index = randint(0, queryset.count()-1)

        return queryset[random_index]
    

class LikeGuidanceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        profile = request.user.profile

        try:
            guidance = Guidance.objects.get(id=id)
        except Guidance.DoesNotExist:
            return Response({"error": "Guidance does not exist of the given ID"}, status=status.HTTP_404_NOT_FOUND) 
        
        if profile in guidance.favorite_users.all():
            return Response({"error": "The user already like this guidance"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            profile.favorite_guidances.add(guidance)
            return Response({"message": "User successfully like this guidance."}, status=status.HTTP_200_OK)