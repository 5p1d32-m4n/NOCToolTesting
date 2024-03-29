from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'templates/index.html')


def login(request):
    pass


def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('template/index.html')
    else:
        form = UserCreationForm()

    return render(request, 'template/registration/userCreate.html', {'form': form})
