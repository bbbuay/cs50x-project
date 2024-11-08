from django.urls import path
from .views import RandomGuidanceDetail, LikeGuidanceView, UnlikeGuidanceView

urlpatterns = [
    path('guidances/random/', RandomGuidanceDetail.as_view(), name='random-guidance-detail'),
    path('guidances/<int:id>/like/', LikeGuidanceView.as_view(), name='like-guidance'),
    path('guidances/<int:id>/unlike/', UnlikeGuidanceView.as_view(), name='unlike-guidance'),
]