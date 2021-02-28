from django.shortcuts import render
from rest_framework.response import Response
import models
import serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView


# Create your views here.
class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fields = ["category", "merchant"]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
