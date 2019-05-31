from django.shortcuts import render, redirect
from .forms import UsersModelForm


def home(request):
	return render(request, 'mainapp/home.html')

def start_training(request):
	return render(request, 'mainapp/start_training.html')

def training(request):
	return render(request, 'mainapp/training.html')