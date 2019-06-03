from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from mainapp.models import UsersModel
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    users = UsersModel.objects.all().order_by('-date')
    count = UsersModel.objects.all().count()

    # Pagination
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users, 'count': count}
    return render(request, "dashboard/dashboard.html", context)