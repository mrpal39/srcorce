from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

def home(request):
   
    return render(request, 'base.html')


# @login_required(login_url='/accounts/login/')
@login_required(redirect_field_name='my_redirect_field')
def my_view(request):
    forms=login()

    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        if not request.user.is_authenticated:
           return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

            # return render(request, 'myapp/login_error.html')

 
def logout_view(request):
    logout(request)