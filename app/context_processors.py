from app import models 


def getlang(request):
    lans = models.Langue.objects.filter(initial__in = ['fr', 'en', 'es', 'pt'])
    data = {
        'langs':lans,
    }
    return data