"""Users Views."""

# Django

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    """Login user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect ('feed')
        else:
            return render(request, 'users/login.html', {'error': 'username or password are invalid'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout user."""
    logout(request)
    return redirect('login')