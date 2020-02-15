from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import User

# Create your views here.
def root(request):
	return redirect('home')

def home(request):
	return render(request, 'homepage.html')

def signup(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	password = request.POST.get('password')

	user = User.objects.filter(email=email)

	if len(user) == 0:
		User.objects.create(name=name, email=email, password=password)
		return redirect('home')
	else:
		return render(request, 'error.html', {'message': 'Account with same email already exists'})


def login(request):
	email = request.POST.get('email')
	password = request.POST.get('password')

	user = User.objects.filter(email=email, password=password)
	if len(user) != 0:
		request.session['email'] = email
		request.session['name'] = user[0].name

		return render(request, 'account.html')

	else:
		return render(request, 'error.html', {'message': 'Account does not exist!'})

def logout(request):
	del request.session['email']
	del request.session['name']

	return redirect('home')