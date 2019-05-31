from django.urls import path
from . import views

urlpatterns = [
	path('', views.quiz, name='quiz'),
	path('completed/', views.completed, name='completed'),
	path('congrats/', views.congrats, name='congrats'),
]