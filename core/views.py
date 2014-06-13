from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import *
from core.forms import *


BRANDS = {
	"KFC":1,
	"Taco Bell":2,
	"Pizza Hut":3
}


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
def overview(request, filter_value=None):
	branch_filters = ["KFC", "Taco Bell", "Pizza Hut"]
	if filter_value in branch_filters:
		branches = Branch.objects.filter(franchise=BRANDS[filter_value])
	else:
		branches = Branch.objects.all()
	return render(request, 'overview.html', {'overview':True, 'branches':branches})


@login_required
def dashboard(request, filter_value=None):
	branch_filters = ["KFC", "Taco Bell", "Pizza Hut"]
	if filter_value in branch_filters:
		branches = Branch.objects.filter(franchise=BRANDS[filter_value])
	else:
		branches = Branch.objects.all().order_by('-date')
	return render(request, 'dashboard.html', {'branches':branches})


@login_required
def add_branch(request):
	if request.method == "POST":
		form = BranchForm(request.POST)
		lat = request.POST.get('latitude')
		lng = request.POST.get('longitude')
		if form.is_valid():
			branch = form.save(commit=False)
			branch.latitude = lat
			branch.longitude = lng
			branch.save()
			return redirect("/dashboard/")
	else:
		form = BranchForm()

	return render(request, 'forms.html', {'form':form})


@login_required
def edit_branch(request, branch_id):
	instance = Branch.objects.get(id=branch_id)
	if request.method == "POST":
		form = BranchForm(request.POST, instance=instance)
		lat = request.POST.get('latitude')
		lng = request.POST.get('longitude')
		if form.is_valid():
			branch = form.save(commit=False)
			branch.latitude = lat
			branch.longitude = lng
			branch.save()
			return redirect("/dashboard/")
	else:
		form = BranchForm(instance=instance)

	return render(request, 'forms.html', {'form':form})


@login_required
def delete_branch(request, branch_id):
	Branch.objects.get(id=branch_id).delete()
	return redirect('/dashboard/')