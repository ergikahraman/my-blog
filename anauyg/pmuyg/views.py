from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# işlem yapacak fonksiyonlar oluşturulur bu kısımda

def index (request,):
    # render arcılığı ile html dosyalarında oluşturmuş olduğumuz yapıyı gönderiyoruz
    return render (request, "index.html")



def isprogramı (request):
    return render (request, "isprogramı.html")

def fiyatlandırma(request):
    return render (request, "fiyatlandırma.html")

def hizmetler (request): #3d 4d 5d
    
    return render (request, "hizmetler.html")

def hizmetler_detay (request, slug): #3d 4d 5d
   return render (request, "hizmetler_detay.html", {
    "slug": slug
   }
    )
    
    #return render (request, "hizmetler_detay.html",  {"slug": slug})

