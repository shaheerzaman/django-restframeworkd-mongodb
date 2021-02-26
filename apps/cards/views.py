from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = '__all__'
        
class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()



