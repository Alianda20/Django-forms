from django.shortcuts import render
from Djangoforms1.forms import Studentforms

def home(request):
   stud=Studentforms
   return render(request, 'index.html',{'form':stud})