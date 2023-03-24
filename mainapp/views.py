from django.contrib.auth.models import User
from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


class MainListView(ListView):
    model = User
    template_name = 'mainapp/index.html'


class EmailView(View):
    def get(self, request):
        logger.error('JUST POST REQUEST IS ADMITTED!')
        return redirect("mainapp:index")

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            title = f'САЙТ - новое письмо.'
            email_body = f'Имя: {name}\nEmail: {email}\nСообщение: {message}'
            logger.error('SENDING EMAIL')
            send_mail(title, email_body, settings.EMAIL_HOST_USER,
                      ['justitdevelopment@gmail.com'])  # justitdevelopment@gmail.com
        except Exception as e:
            logger.fatal('ERROR:', e)
        else:
            logger.error('EMAIL SENT!')
        return redirect("mainapp:index")
