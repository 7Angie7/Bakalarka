# chat/views.py
from django.shortcuts import render


def admin_page(request):
    return render(request, 'semaphore/admin_page.html')


def index(request):
    return render(request, 'semaphore/index.html')