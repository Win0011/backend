from django.shortcuts import render
from django.http import HttpResponse




def homepage(request):
    # return HttpResponse("<h1>Home Page</h1>")
    return render(request, "store/index.html")     
    #return render(request, response)

