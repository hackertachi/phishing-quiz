from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('start/', views.start_training, name='start-training'),
	path('training/', views.training, name='training'),
	path('page2/', views.page2, name='page2'),
	path('test/', views.test, name='test'),
]