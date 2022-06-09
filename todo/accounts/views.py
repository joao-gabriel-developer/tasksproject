from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    succes_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login')

# Create your views here.
