from django.contrib import admin
from django.contrib.auth.models import User
from .models import BookReaderUser, Book, BookAndBookPackage, BookMaker, OrganizationFinancialAccount,\
    Language, Admin, BookSeller, SellBy, FinancialAccount, BookMakerLanguage, Write, Order, \
    BookShoppingCart, PreOrder, BookRating, BookMakerRating, TranslationRequest, Income, Expense, BookPackage, \
    BookComment, CommentReply
# Register your models here.
# admin.site.register(User)
admin.site.register(BookReaderUser),
admin.site.register(Book),
admin.site.register(BookAndBookPackage),
admin.site.register(BookMaker),
admin.site.register(OrganizationFinancialAccount),
admin.site.register(Language),
admin.site.register(Admin),
# admin.site.register(Genre),
admin.site.register(BookSeller),
admin.site.register(SellBy),

