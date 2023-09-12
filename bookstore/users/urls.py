from django.urls import path
from  .views import userView, SignupPageView

urlpatterns = [
    path('',userView, name='user'),
    path('signup/',SignupPageView.as_view(), name="signup")
]