from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    context = {'pythons': pythons}
    return render(req, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', {'form': form})
