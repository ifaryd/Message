from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.translation import ugettext as _
from . import models 
from django.db.models import Q
# Create your views here.
def accueil(request):
    currentpage = ""
    return redirect('/fr/')

def index(request, lang):
    lang = lang
    currentpage = ""
    
    # actus = models.Actualite.objects.all()[:3]
    return render(request, 'index.html', locals())



def result(request, lang):
    lang = lang
    currentpage = ""
    
    # actus = models.Actualite.objects.all()[:3]
    return render(request, 'result.html', locals())




def contact(request, lang):
    lang = lang
    currentpage = ""
    return render(request, 'contact.html', locals())

def predications_lists(request, lang):
    lang = lang
    currentpage = "predications"
    
    search_query = request.GET.get('search', '')
    if search_query:
        predications = models.Predication.objects.filter(Q(titre__icontains = search_query) | Q(nom_pred__icontains = search_query), id_langue__initial = lang)
    else:
        predications = models.Predication.objects.filter(id_langue__initial = lang)

    paginator = Paginator(predications, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1     
    try:
        predications = paginator.page(page)
    except(EmptyPage, InvalidPage):
        predications = paginator.page(paginator.num_pages)

    return render(request, 'predications-lists.html',  locals())

def predications_detail(request, lang, predid):
    lang = lang
    currentpage = "predication/"+ str(predid)
    predications = models.Predication.objects.get(pk =int(predid))
    versets =  models.Verset.objects.filter(id_pred = predications)
    pred_next = str(int(predid) +1 )
    pred_prev = str(int(predid) -1 )
    return render(request, 'predications-details.html', locals())