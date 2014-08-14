from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models import Q
from random import randint
from core.models import *
from core.forms import *


def home(request):
	if request.user.is_authenticated():
		return redirect('/overview/')

	try:
		login_picture = LoginPicture.objects.all().order_by('-id')[0]
	except:
		login_picture = None

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

	return render(request, 'login.html', {'error':error, 'login_picture':login_picture})


def logout_aux(request):
	logout(request)
	return redirect('/')


@login_required
def overview(request, filter_value=None):
	branch_filters = ["KFC", "Taco Bell", "Pizza Hut"]
	if filter_value in branch_filters:
		branches = Branch.objects.filter(franchise=Brand.objects.get(name=filter_value))
	else:
		branches = Branch.objects.all()
	competitors = Competitor.objects.all()
	brands = Brand.objects.all()
	return render(request, 'overview.html', {'overview':True, 'branches':branches, 'brands':brands, 'competitors':competitors})


@login_required
def dashboard(request, filter_value=None):
	branch_filters = ["KFC", "Taco Bell", "Pizza Hut"]
	search_value = None
	if filter_value in branch_filters:
		branches = Branch.objects.filter(franchise=Brand.objects.get(name=filter_value))
	else:
		branches = Branch.objects.all().order_by('-date')

	if request.method == 'POST':
		search_value = request.POST.get('search')
		branches = branches.filter(
				Q(name__icontains=search_value) |
				Q(contact_name__icontains=search_value) |
				Q(phone__icontains=search_value) |
				Q(email__icontains=search_value) |
				Q(owner_name__icontains=search_value) |
				Q(operator_name__icontains=search_value) |
				Q(address__icontains=search_value)
			).order_by('-date')
	brands = Brand.objects.all()
	return render(request, 'dashboard.html', {'branches':branches, 'brands':brands, 'search_value':search_value})


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


def forgot_password(request):
	answer = None
	if request.method == "POST":
		email = request.POST.get("email")
		try:
			user = User.objects.get(email=email)
			new_password = randint(100000, 999999)
			message = "Hello, \nThis is an answer to password recovery. Please change your password for security reasons.\nNew Password: "+str(new_password)
			email = EmailMessage('Yum! Brands', message, to=[email])
			email.send()
			user.set_password(new_password)
			user.save()
			answer = "The password was sent to you email."
		except:
			answer = "There are no accounts registered in this email."

	return render(request, 'login.html', {'forgot_password':True, 'answer':answer})


@login_required
def change_password(request):
	error = None
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if not request.user.check_password(request.POST.get('old_password')):
			error = "Wrong old password"
		else:
			if form.is_valid():
				request.user.set_password(request.POST.get('password1'))
				request.user.save()
				return redirect('/')
	else:
		form = ChangePasswordForm()
	return render(request, 'forms.html', {'change_password':True, 'form':form, 'error':error})


