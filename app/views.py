from socket import NI_NUMERICHOST
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.translation import ugettext as _
from . import models 
from django.db.models import Q

# Create your views here.
# actus = models.Actualite.objects.all()[:3]

def accueil(request):
    currentpage = ""
    return redirect('/fr/')


def index(request, lang):
    lang = lang
    currentpage = ""
    predications = models.Predication.objects.filter(id_langue__initial = lang).all().order_by('-_id') [:3]
    return render(request, 'index.html', locals())


def result(request, lang):
    lang = lang
    currentpage = ""
    predications = models.Predication.objects.filter(id_langue__initial = lang)
    versets =  models.Verset.objects.filter(id_langue__initial = lang)

    search_query = request.GET.get('search', '')
    if  search_query:
        versets = models.Verset.objects.filter(Q(contenu__icontains = search_query), id_langue__initial = lang)
    else:
        versets = models.Verset.objects.filter(id_langue__initial = lang)
    
    paginator = Paginator(versets, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        versets = paginator.page(page)
    except(EmptyPage, InvalidPage):
        versets = paginator.page(paginator.num_pages)

    paginator = Paginator(predications, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        predications = paginator.page(page)
    except(EmptyPage, InvalidPage):
        predications = paginator.page(predications.num_pages)
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


def predications_detail(request, lang, num_pred):
    lang = lang
    currentpage = "predication/"+ str(num_pred)
    predications = models.Predication.objects.filter(numero =int(num_pred),id_langue__initial = lang).first()
    if predications:
        versets =  models.Verset.objects.filter(id_langue__initial = lang, num_pred__numero = int(num_pred))
        pred_next = str(int(num_pred) +1)
        pred_nexto = models.Predication.objects.get(pk = pred_next)
        pred_prev = str(int(num_pred) -1)
        if  int(num_pred) == 1:
            print("pas")
        else:
            pred_prevo = models.Predication.objects.get(pk = pred_prev)
        # pred = str(int(predid))
        # pred_lien = models.Predication.objects.get(pk = pred)
        print(lang)
        print(num_pred)
        # print(predications)
        print(predications.pred_verset.all())
        # print(versets)

        return render(request, 'predications-details.html', locals())

    else:
        return redirect('accueil')











    
    