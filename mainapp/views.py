from django.shortcuts import render
from .models import News

def home(request):
    arr = [i for i in range(1, 30) if i != 8 and i != 2]
    context = {
        'range': arr,
        'news': News.objects.all()
    }
    return render(request, 'index.html', context)