from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('get_index'))
    
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
                # change to get_index 160220
                return redirect(reverse('get_index'))
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
            
            # change to get_index 160220
            return redirect(reverse('get_index'))
    else:
        register_form = UserRegistrationForm()
    return render(request, 'Accounts/register.template.html', {'form':register_form})
    
@login_required
def view_profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your profile is succesfully updated!')  
            return redirect(reverse('view_profile'))
    else:
        u_form = UserUpdateForm(instance=request.user)
        
    return render(request, 'Accounts/profile.template.html', {
        'u_form': u_form,
        'current_user':request.user
    })

        
        
    
    