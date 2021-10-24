from django.contrib.auth.models import User
#from rest_framework import viewsets
from rest_framework import permissions 
from main.serializers import UserSerializer
from rest_framework.views import APIView

class User(APIView):
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    print('Please wait while the program is loading...')
