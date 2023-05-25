from django.shortcuts import render
from .models import *


def main_page(request):
    em = Users.objects.all()
    context = {"mails": em}
    return render(request, "MainPage/index.html", context=context)
