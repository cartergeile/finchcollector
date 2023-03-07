from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# lists of dummy finches
#
  #{'name': 'Lolo', 'description': 'furry little demon', 'age': 3},
  #{'name': 'Sachi', 'description': 'gentle and loving', 'age': 2},
#]

# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# about route
def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'