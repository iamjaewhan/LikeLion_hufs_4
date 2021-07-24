from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignupForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
                request=request,
                username=name,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                return redirect('index')

        return redirect('account:login')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request = request, data=request.POST)
#         if form.is_valid():
#             name = request.POST['name']
#             password = request.POST['password']
#             user = auth.authenticate(
#                 request,
#                 name=name,
#                 password=password
#             )
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('home')
#             return redirect('account:login')
#         else:
#             form = AuthenticationForm()
#             return render(request, 'login.html', {'error': 'name or password is incoreect'})

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(name=request.POST['name'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
        
        return render(request, 'signup.html')
    
    else:
        form=SignupForm()
        return render(request, 'signup.html', {'form':form})