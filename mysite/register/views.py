from django.shortcuts import render, redirect
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from register.models import LoginModel
from register.serializers import RegisterSerializer
from rest_framework.decorators import api_view
# import request
# import json 
from bs4 import BeautifulSoup
# import html_to_json
from django.views.decorators.csrf import csrf_protect

#this is the view function of the registration inherited from the original django
def register(response):
    form = UserCreationForm()
    return render(response, "register/register.html", {"form": form})

        
from .models import User  # Make sure you import your User model
from .serializers import RegisterSerializer

@csrf_protect
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)  # Use request.data
        if serializer.is_valid():
            # Create a new User instance here
            User.objects.create(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

