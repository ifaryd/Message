from django.shortcuts import render, redirect
from . import models 
# Create your views here.
def accueil(request):
    currentpage = ""
    return redirect('/fr/')

def index(request, lang):
    lang = lang
    currentpage = ""
    
    # actus = models.Actualite.objects.all()[:3]
    return render(request, 'index.html', locals())

def contact(request, lang):
    lang = lang
    currentpage = ""
    return render(request, 'contact.html', locals())

def predications_lists(request, lang):
    lang = lang
    currentpage = "predications"
    predications = models.Predication.objects.filter(id_langue__initial = lang)

    return render(request, 'predications-lists.html', locals())

def predications_detail(request, lang, predid):
    lang = lang
    currentpage = "predication/"+ str(predid)
    predications = models.Predication.objects.get(pk =int(predid))
    versets =  models.Verset.objects.filter(id_pred = predications)
    pred_next = str(int(predid) +1 )
    return render(request, 'predications-details.html', locals())