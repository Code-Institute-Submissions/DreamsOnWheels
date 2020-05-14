from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


@login_required
def logout(request):
    """
    Logout the user
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect(reverse('index'))

def login(request):
    """
    Return a login page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is incorrect!')
    else:
        login_form = UserLoginForm()
        context = {
            'login_form': login_form,
            'login_page': 'active'
        }
    return render(request, 'login.html', context)


def register(request):
    """
    A view that manages the registration form
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
            else:
                messages.error(request, 'Unable to log you in at this time!')
    else:
        user_form = UserRegistrationForm()
    context = {
        'user_form': user_form,
        'register_page': 'active'}
    return render(request, 'register.html', context)

@login_required
def user_profile(request):
    """
    Get the user profile page
    """
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(username=request.user.username)
    context = {
        'profile': user,
        'profile_page': 'active'
    }
    return render(request, 'profile.html', context)