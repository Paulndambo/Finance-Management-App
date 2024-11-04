from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from users.models import User
from users.serializers import RegisterSerializer

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "account/login.html")


def user_logout(request):
    logout(request)
    return redirect("/")

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RegisterUserAPIView(APIView):
    serializer_class = RegisterSerializer
    
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello World!!"}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        user = User.objects.create(
            username=request.data.get("username"),
            email=request.data.get("email"),
            password=request.data.get("password"),
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            phone_number=request.data.get("phone_number"),
            role=request.data.get("role"),
            gender=request.data.get("gender"),
        )
        user.set_password(user.password)
        user.save()
        return Response({"message": "Hello World!!"}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Something Went Wrong!!"}, status=status.HTTP_400_BAD_REQUEST)