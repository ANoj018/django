from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def create(request):
    return HttpResponse("Create User View")

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        Users.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

