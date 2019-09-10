from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.

def login_auth(request):
	result = {}
	return render(request, 'login.html', result)
