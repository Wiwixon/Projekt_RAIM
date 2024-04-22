import joblib
from django.shortcuts import render
from django.http import HttpResponse, request
import numpy as np
from matplotlib.style import context


def index(request):
    return render(request, 'ann.html')

