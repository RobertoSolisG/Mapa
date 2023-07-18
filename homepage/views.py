from django.shortcuts import render
from django.http import JsonResponse
from .models import Curso


# Create your views here.
#def home(request):
 #   return render(request,'homepage/home2.html')



def home(request):
    cursolistados = Curso.objects.all().order_by('id', '-creditos')
    assert isinstance(request, object)
    return render (request,'homepage/home10.html',  {'cursos':cursolistados})




