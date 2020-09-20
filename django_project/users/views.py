from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):

    if request.method == 'POST':
        # create a form with data entered by user
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save user (auto hashes pw)
            form.save()
            # extract username and flash success
            username = form.cleaned_data.get("username") #clean_data dict
            messages.success(request, f'Account created for {username}. Please log in.')
            
            return redirect('login')
    else:
        # create a blank registration form with django forms
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    if request.method == 'POST':
        # these will be rendered together and look like one form in our profile.html
        # each form expects an instance of a model (user, and profile) and will
        # auto populate the form with associated details
        user_u_form = UserUpdateForm(request.POST, 
                                     instance=request.user)
        profile_u_form = ProfileUpdateForm(request.POST,
                                           request.FILES, 
                                           instance=request.user.profile)
    
        if user_u_form.is_valid() and profile_u_form.is_valid():
            user_u_form.save()
            profile_u_form.save()

            messages.success(request, f'Your account has been updated')
            
            return redirect('profile')
    else:
        user_u_form = UserUpdateForm(instance=request.user)
        profile_u_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_u_form': user_u_form,
        'profile_u_form': profile_u_form
    }

    return render(request, 'users/profile.html', context)

