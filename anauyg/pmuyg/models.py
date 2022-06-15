
from django.db import models
from django.forms import ModelChoiceField




class Malzeme (models.Model):
    mal_rayic = models.CharField(max_length= 15)
    mal_tanım = models.CharField(max_length= 100)
    mal_miktar = models.DecimalField(max_digits=5, decimal_places=3)
    mal_fiyat = models.DecimalField(max_digits= 10, decimal_places= 3)

class Makine (models.Model):
    mak_rayic = models.CharField(max_length= 15)
    mak_tanım = models.CharField(max_length= 100)
    mak_miktar = models.DecimalField(max_digits=5, decimal_places=3)
    mak_fiyat = models.DecimalField(max_digits= 10, decimal_places= 3)

class İscilik (models.Model):
    is_rayic = models.CharField(max_length= 15)
    is_tanım = models.CharField(max_length= 100)
    is_miktar = models.DecimalField(max_digits=5, decimal_places=3)
    is_fiyat = models.DecimalField(max_digits= 10, decimal_places= 3)


class Birim (models.Model):
    birim = models.CharField(max_length= 3)
    

class BirimFiyat (models.Model):
    poz_no = models.CharField(max_length= 15)
    tanım = models.CharField(max_length= 100)
    
    fiyat = models.DecimalField(max_digits= 10, decimal_places= 3)
    slug = models.SlugField(unique= True) 
    # unique=true yaparak hiçbir alandaki bilgi diğeriyle aynı olmayacak.
    malzeme = models.ForeignKey(Malzeme, on_delete=models.CASCADE)
    makine = models.ForeignKey(Makine, on_delete=models.CASCADE)
    iscilik = models.ForeignKey(İscilik, on_delete=models.CASCADE)
    birim = models.ForeignKey(Birim, on_delete=models.CASCADE)

    
# Create your models here.
