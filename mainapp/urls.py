from django.urls import path
from mainapp.views import MainListView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
]