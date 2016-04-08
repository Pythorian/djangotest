from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def pagina_inicial(request):
    return render(request, 'blog/index.html', {})