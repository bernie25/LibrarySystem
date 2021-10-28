# from rest_framework.views import APIView
# from .models import LibrarySystem
# from .serializers import LibrarySystemSerializer
# from rest_framework import viewsets 
# from django.shortcuts import render

# class LibrarySystemView(APIView):
#     serializer_class = LibrarySystemSerializer
#     queryset = LibrarySystem.objects.all()
    
#     # def get(self, request, *args, **kwargs):
#     #         """This is to fetch the list."""
#     #         return Response()
    
#     # def home(request):      
#     #     return render(request=request, template_name="user.html")


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")