from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views import generic

from .forms import CustomUserCreationForm
# Create your views here.

def userView(request):
    return HttpResponse('Hello World!')

class SignupPageView(generic.CreateView):
    form_class=CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

