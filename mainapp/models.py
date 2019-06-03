from django.db import models
from datetime import datetime


class UsersModel(models.Model):
	department_choices = (
		('Finance', 'Finance'),
		('Credit and Risk', 'Credit and Risk'),
		('Sales and Collection', 'Sales and Collection'),
		('IT', 'IT'),
		('Sales Operations', 'Sales Operations'),
		('Consumer Loans', 'Consumer Loans'),
		('Documentation and Records', 'Documentation and Records'),
		('HRAD', 'HRAD'),
		('Spare Parts', 'Spare Parts'),
		('Supply Chain', 'Supply Chain'),
		('Audit', 'Audit'),
		('Service', 'Service'),
		('Engineering', 'Engineering'),
		('Treasury', 'Treasury'),
		('Marketing', 'Marketing'),
		('Legal', 'Legal'),
		('Operations', 'Operations'),
		('Insurance', 'Insurance'),
		('Tax Compliance', 'Tax Compliance'),
		('Financial Planning', 'Financial Planning'),
		('Opcom', 'Opcom'),
	)


	date = models.DateTimeField(default=datetime.now)
	name = models.CharField(max_length=40, verbose_name="Full Name")
	department = models.CharField(max_length=40, choices=department_choices, verbose_name="Department")
	email = models.EmailField(max_length=100, verbose_name="Email")

	def __str__(self):
		return self.name