from django.shortcuts import render
from django.views import generic
from .models import Response
from .forms import ResponseCreateForm
from django.urls import reverse, reverse_lazy

# Create your views here.

class HomePageView(generic.CreateView):
	model = Response
	form_class = ResponseCreateForm
	template_name = 'zuriprofilecard.html'
	success_url = reverse_lazy('response-success')

class SuccessResponseView(generic.TemplateView):
	template_name = 'success_response.html'