from django.shortcuts import render
#from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = '__all__'
        
class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('question_type', )
    search_fields = ('question', )
    ordering = ('question_type', )



