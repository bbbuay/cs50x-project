from django.urls import path
from .views import RandomGuidanceDetail, LikeGuidanceView

urlpatterns = [
    path('guidances/random/', RandomGuidanceDetail.as_view(), name='random-guidance-detail'),
    path('guidances/<int:id>/like/', LikeGuidanceView.as_view(), name='like-guidance')
]