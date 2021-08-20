from django import forms
from .models import Response

class ResponseCreateForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ('name','email','response')
		widgets = {
		'name': forms.TextInput(),
		'email': forms.TextInput(attrs={'style':"clear:both;"}),
		'response': forms.Textarea(attrs={'class':'text-area', 'placeholder':'Write Something...', 'style':" width: 200px;height: 200px;"}),
		}