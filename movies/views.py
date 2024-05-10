from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def index(request):
    output =' '.join([movie.title for movie in Movie.objects.all()])
    # return HttpResponse(output)
    return render(request,'./index.html',{'movies':Movie.objects.all()})

def details(request,movie_id):
    return render(request,'./details.html',{'movie':Movie.objects.get(id=movie_id)})