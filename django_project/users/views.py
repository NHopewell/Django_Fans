from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':
        # create a form with data entered by user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_data.get("username") #clean_data dict
            messages.success(request, f'Account created for {username}.')
            
            return redirect('blog-home')
    else:
        # create a blank registration form with django forms
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

