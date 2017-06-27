from django.contrib import admin
from aparcamientos.models import Parking, Users_Page, Users_Favs, Comment


# Register your models here.
admin.site.register(Parking)
admin.site.register(Users_Page)
admin.site.register(Users_Favs)
admin.site.register(Comment)
