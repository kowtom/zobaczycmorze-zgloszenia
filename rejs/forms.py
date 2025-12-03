from django import forms
from .models import Zgloszenie

class ZgloszenieForm(forms.ModelForm):
	class Meta:
		model = Zgloszenie
		fields = ['imie', 'nazwisko', 'email', 'telefon', 'wzrok']
		