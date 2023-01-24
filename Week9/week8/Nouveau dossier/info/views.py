from django.shortcuts import render

from info.models import Locataire


def index(request):
    locataires = Locataire.objects.all()
    context = {"locataires":locataires}
    return render(request, 'info/index.html', context)

# Create your views here.
