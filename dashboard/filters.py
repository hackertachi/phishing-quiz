from mainapp.models import UsersModel
import django_filters

class UsersFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
	class Meta:
		model = UsersModel
		fields = ['name', 'department', 'email']