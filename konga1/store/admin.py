from django.contrib import admin
from store.models import product
from django.http import HttpResponse



admin.site.register(product)

def home(request):
    pass


