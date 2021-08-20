from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home-page'),
	path('response/success', views.SuccessResponseView.as_view(), name='response-success')
]