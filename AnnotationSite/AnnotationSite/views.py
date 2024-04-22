from django.shortcuts import render
from django.http import HttpResponse
from .models import Selection
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request, 'ann.html')


def save_selection(request):
    if request.method == 'POST':
        image_data = request.POST.get('imageData')
        x = request.POST.get('x')
        y = request.POST.get('y')
        width = request.POST.get('width')
        height = request.POST.get('height')

        # Zapisanie danych w bazie danych
        selection = Selection.objects.create(image_data=image_data, x=x, y=y, width=width, height=height)

        return HttpResponse("Selection saved successfully!")
    else:
        return HttpResponse("Invalid request method")

def display_images(request):
    images = Selection.objects.all()
    return render(request, 'display_images.html', {'images': images})