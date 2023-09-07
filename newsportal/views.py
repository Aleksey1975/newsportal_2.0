from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import *
#from .filters import *
#from .forms import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


def index(request):
    return render(request, 'index.html')
