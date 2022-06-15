from django.contrib import admin

from pmuyg.models import Birim, BirimFiyat, Makine, Malzeme, İscilik

# Register your models here.


admin.site.register(BirimFiyat)
admin.site.register(Malzeme)
admin.site.register(İscilik)
admin.site.register(Makine)
admin.site.register(Birim)