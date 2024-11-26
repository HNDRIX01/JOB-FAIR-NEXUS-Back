from django.urls import path
from .views import HelloWorldView, InsightView, UserProfileCreateView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('insights/', InsightView.as_view(), name='insights'),
    path('user-profile/', UserProfileCreateView.as_view(), name='user-profile-create'),
]
