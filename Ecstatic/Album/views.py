from django.shortcuts import render, redirect
from .models import Album

# Create your views here.
def index(request):
    return render(request, 'index.html')

def album(request):
    Images = Album.objects.all().order_by('date')
    context = {
        'Images': Images
    }
    return render(request, 'album.html', context)

def image_card(request, title):
    image = Album.objects.get(title=title)
    context = {
        'image': image
    }
    return render(request, 'card.html', context)