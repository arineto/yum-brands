from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
	if request.user.is_authenticated():
		return redirect('/overview/')

	error = None
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	      if user.is_active:
	        login(request, user)
	        return redirect('/overview/')
	      else:
	      	error = "Not active user"
	    else:
	    	error = "Invalid username/password"

	return render(request, 'login.html', {'error':error})


def logout_aux(request):
	logout(request)
	return redirect('/')


@login_required
def overview(request):
	return render(request, 'overview.html', {'overview':True})


@login_required
def dashboard(request):
	return render(request, 'dashboard.html', {})
