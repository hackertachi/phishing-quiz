from django.shortcuts import render, redirect
from .forms import UsersModelForm


def home(request):
	return render(request, 'mainapp/home.html')

def start_training(request):
	if request.method == 'POST':
		usersmodelform = UsersModelForm(request.POST)
		if usersmodelform.is_valid():
			usersmodelform.save()
			return redirect('training')

	usersmodelform = UsersModelForm()
	context = {'usersmodelform': usersmodelform}
	return render(request, 'mainapp/start_training.html', context)

def training(request):
	return render(request, 'mainapp/training.html')

def page2(request):
	return render(request, 'mainapp/page2.html')
