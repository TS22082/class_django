from django.shortcuts import render
from .models import List

# Create your views here.

def home(request):
    todo_list = List.objects.all
    return render(request, 'home.html', {"todo_list" : todo_list})