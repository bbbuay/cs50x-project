from django.urls import path
from .views import RandomGuidanceDetail

urlpatterns = [
    path('guidances/random/', RandomGuidanceDetail.as_view(), name='random-guidance-detail')
]