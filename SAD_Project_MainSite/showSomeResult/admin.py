from django.contrib import admin

# Register your models here.
from .models import TopGenre, BookForTarjome

admin.site.register(TopGenre)
admin.site.register(BookForTarjome)
