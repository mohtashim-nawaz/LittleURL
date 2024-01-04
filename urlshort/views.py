from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from . import models
from django.views.decorators.csrf import csrf_exempt
import random, string
from datetime import datetime
# Create your views here.

DEFAULT_URL = "http://127.0.0.1:8000/"

def home(request):
    return render(request, 'home.html')

def my_redirect(request, url):
    current_obj = models.ShortURL.objects.filter(short_url=url)
    if len(current_obj)==0:
        return HttpResponseNotFound()
    ret = current_obj[0].original_url
    return redirect(ret)
    #return HttpResponse("<a href="+ret+" target=_blank>"+ret+"</a>")
   
@csrf_exempt  
def createShortURL(request):
    if request.method == 'POST':
        original_url = request.POST['Original URL']

        current_obj = models.ShortURL.objects.filter(original_url=original_url)
        if len(current_obj)!=0:
            ret = DEFAULT_URL+current_obj[0].short_url
            return HttpResponse("<a href="+ret+" target=_blank>"+ret+"</a>")

        random_char_list = list(string.ascii_letters)
        random_chars = ''
        for i in range(6):
            random_chars+= random.choice(random_char_list)

        while len(models.ShortURL.objects.filter(short_url=random_chars))!=0:
            for i in range(3):
                random_chars+= random.choice(random_char_list)

        currDateTime = datetime.now()
        newShortURL = models.ShortURL(original_url=original_url, short_url=random_chars, date_time_created = currDateTime)  
        newShortURL.save()

        ret = DEFAULT_URL+newShortURL.short_url
        return HttpResponse("<a href="+ret+" target=_blank>"+ret+"</a>")
    else:
        return HttpResponseBadRequest("Bad Request")