from django.urls import path
from .views import RandomGuidanceDetail, LikeGuidanceView, UnlikeGuidanceView
from .views import homepage_view

urlpatterns = [
    path('', homepage_view, name='homepage'),
    
    # api endpoints
    path('api/guidances/random/', RandomGuidanceDetail.as_view(), name='random_guidance_detail'),
    path('api/guidances/<int:id>/like/', LikeGuidanceView.as_view(), name='like_guidance'),
    path('api/guidances/<int:id>/unlike/', UnlikeGuidanceView.as_view(), name='unlike_guidance'),
]