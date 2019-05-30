from django import forms
from .models import UsersModel

class UsersModelForm(forms.ModelForm):
	class Meta:
		model = UsersModel
		fields = ['name', 'department', 'email']