from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

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
            messages.success(request, f'Account created for {username}.')
            
            return redirect('blog-home')
    else:
        # create a blank registration form with django forms
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

