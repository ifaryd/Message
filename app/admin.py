from django.contrib import admin

from .models import Predication, Langue, Verset
# Register your models here.
admin.site.register(Predication)
admin.site.register(Langue)
admin.site.register(Verset)