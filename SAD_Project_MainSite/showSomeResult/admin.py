from django.contrib import admin

# Register your models here.
from .models import TopGenre, BookForTarjome, motarjem

# admin.site.register(TopGenre)
admin.site.register(BookForTarjome)
# admin.site.register(motarjem)

########################
##### Hamid's Models
########################
from .models import BookReaderUser, Language, Book, Genre, BookSeller, BookMaker, TranslationRequest#, BookMakerLanguage
from .models import Notification

admin.site.register(Notification)
admin.site.register(BookReaderUser)
admin.site.register(Language)

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookSeller)

admin.site.register(BookMaker)
# admin.site.register(BookMakerLanguage)
admin.site.register(TranslationRequest)