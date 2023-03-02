from django.shortcuts import render


# lists of dummy finches
finches = [
  {'name': 'Lolo', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# about route
def about(request):
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })