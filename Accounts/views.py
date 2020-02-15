from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(reverse('show_books'))
    
def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            # authentication of user
            user = auth.authenticate(username=username, password=password)
            
            # if authentication is successful
            if user:
                auth.login(request=request, user=user)
                messages.success(request, 'You have successfully logged in.')
                return redirect(reverse('show_books'))
            else:
                login_form.add_error(None, 'Invalid username or password.')
    else:
        login_form = UserLoginForm()
    
    return render(request, 'Accounts/login.template.html', {'form':login_form})
    
def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()    
            
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            messages.success(request, 'Registration successful!')
            
            auth.login(request=request, user=user)
            
            return redirect(reverse('show_books'))
    else:
        register_form = UserRegistrationForm()
    return render(request, 'Accounts/register.template.html', {'form':register_form})
    
@login_required
def profile(request):
    return render(request, 'Accounts/profile.template.html', {
        'current_user':request.user
    })