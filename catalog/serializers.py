from rest_framework import serializers
from .models import Book


class Book_API(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'