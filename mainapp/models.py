from django.db import models


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


	name = models.CharField(max_length=30, verbose_name="Name")
	department = models.CharField(max_length=20, choices=department_choices, verbose_name="Department")
	email = models.EmailField(max_length=30, verbose_name="Email")