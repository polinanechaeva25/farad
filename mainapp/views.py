from django.contrib.auth.models import User
from django.views.generic import ListView


class MainListView(ListView):
    model = User
    template_name = 'mainapp/index.html'
