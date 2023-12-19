from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from blog.models import CustomUser
from .serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.

class UserView(APIView):
    def get(self, request):
        output = [
            {
                'username' : output.username,
                'email' : output.email,
                'password' : output.password,
                'isAdmin' : output.isAdmin,
                'welcomeCode' : output.welcomeCode,
            } for output in CustomUser.objects.all()
        ]
        return Response(output)
    
    def post(self,  request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

