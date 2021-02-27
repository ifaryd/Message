from django.shortcuts import render, redirect
from . import models
# Create your views here.
def accueil(request):
    
    return redirect('/fr/')

def index(request, lang):
    #predication = models.Predication.objects.language('fr')[:1].get()
    #verset = models.Verset.objects.language(predication.get_current_language())[:1].get()
    lang = lang
    return render(request, 'index.html', locals())


def contact(request, lang):
    lang = lang
    return render(request, 'contact.html', locals())

def predications_lists(request, lang):
    lang = lang
    
    predications = models.Predication.objects.filter(id_langue__initial = lang)
    return render(request, 'predications-lists.html', locals())


def predications_detail(request, lang, predid):
    lang = lang
    
    predications = models.Predication.objects.filter(id_langue__initial = lang)
    return render(request, 'predications-details.html', locals())