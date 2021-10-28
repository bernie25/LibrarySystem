from .models import LibrarySystem
from rest_framework import serializers

class LibrarySystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LibrarySystem
        fields = ['id', 'title']
