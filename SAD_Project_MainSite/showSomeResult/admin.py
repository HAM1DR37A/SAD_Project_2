from django.contrib import admin

# Register your models here.
from .models import TopGenre, BookForTarjome, motarjem

admin.site.register(TopGenre)
admin.site.register(BookForTarjome)
admin.site.register(motarjem)