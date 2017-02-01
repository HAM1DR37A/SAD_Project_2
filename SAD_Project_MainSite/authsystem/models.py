from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.fields.related import ForeignKey


# class Avatar(models.Model):
#     avatar_id = models.CharField(primary_key=True, auto_created=True)
#     avatar_image = models.ImageField(null=False)


class BookReaderUser(models.Model):
    django_user = models.OneToOneField(User, null=False)
    avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=True)
    birth_date_month = models.CharFieldField(max_length=2)
    birth_date_day = models.CharField(max_length=2)
    birth_date_day = models.CharField(max_length=4)

    def __str__(self):
        return str(self.id)


class OrganizationFinancialAccount(models.Model):
    account_id = models.IntegerField(primary_key=True)


class Language(models.Model):
    language_name = models.CharField(max_length= 10)


class Admin(models.Model):
    django_user = models.OneToOneField(User, null=False)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=40, null=False)
    first_publish_year = models.IntegerField(null=False)
    isbn = models.CharField(max_length=20, null=False, unique=True)
    number_of_pages = models.IntegerField()
    summary = models.TextField()
    cover_image_addr = models.ImageField(null=False, default='Book.png')
    author_name = models.CharField(null=False, max_length=20, default='author')
    translator_name = models.CharField(null=True, max_length=20)
    publisher_name = models.CharField(null=True, max_length=20)
    adding_date = models.DateTimeField(default=timezone.now())


# this entity is the genre
class Genre(models.Model):
    genre_type = models.CharField(max_length=20,null=False, primary_key=True)


# this entity represents relation between book and genre
class GenreBook(models.Model):
    genre_type = models.ForeignKey(Genre, on_delete= models.PROTECT)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('genre_type', 'book_id')


class BookSeller(models.Model):
    django_user = models.OneToOneField(User, null=False)
    avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=False)
    is_verified = models.BooleanField(default=False)
    birth_date_month = models.CharFieldField(max_length=2)
    birth_date_day = models.CharField(max_length=2)
    birth_date_day = models.CharField(max_length=4)

    def __str__(self):
        return str(self.id)



class SellBy(models.Model):
    price = models.FloatField(null= False)
    number_of_copies = models.IntegerField(null=False)
    book_seller_id = models.ForeignKey(BookSeller, on_delete=models.CASCADE, null=False)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('book_id', 'book_seller_id')


class BookMaker(models.Model):
    male = 'ML'
    female = 'FM'
    translator = 'TR'
    author = 'AUT'
    both = 'Both'
    gender_choices = (
        (male, 'Male'),
        (female, 'Female')
    )
    type_choices = (
        (translator, "Translator"),
        (author, "Author"),
        (both, "Both")
    )
    django_user = models.OneToOneField(User, null=False)
    birth_date_month = models.CharFieldField(max_length=2)
    birth_date_day = models.CharField(max_length=2)
    birth_date_day = models.CharField(max_length=4)
    gender = models.CharField(max_length=2, choices=gender_choices, null=False)
    book_maker_type = models.CharField(max_length=4, choices=type_choices, null=False)
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(null=False, default='user.png')
    telephone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150, null=False)

    def __str__(self):
        return str(self.id)


class FinancialAccount(models.Model):
    # ****book_seller_id and book_maker_id can't be null at the same time****
    account_no = models.CharField(max_length=20)
    book_seller_id = models.ForeignKey(BookSeller, on_delete=models.CASCADE)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)


class BookMakerLanguage(models.Model):
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)
    language_name = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book_maker_id', 'language_name')


class Write(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book_id', 'book_maker_id')


class Order(models.Model):
    delivery_date = models.DateTimeField(null=True)
    order_date = models.DateTimeField(default=timezone.now())


class BookOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)


class BookShoppingCart(models.Model):
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT)
    book_id = models.ForeignKey(SellBy, on_delete=models.PROTECT)


class PreOrder(models.Model):
    # author can be retrieved by access to Write table
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    user_name = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        unique_together = ('book_id', 'user_name')


class BookRating(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(BookReaderUser, on_delete= models.CASCADE)
    Score = models.IntegerField(null= False)

    class Meta:
        unique_together = ('book_id', 'user_id')


class BookMakerRating(models.Model):
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.CASCADE)
    date = models.DateField()
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    Score = models.IntegerField()

    class Meta:
        unique_together = ('book_maker_id', 'user_id')


class TranslationRequest(models.Model):
    book_file = models.FileField()
    book_name = models.CharField(max_length=50, null=False)
    source_lang = models.ForeignKey(Language,null=False)
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT)
    book_maker_id = models.ForeignKey(BookMaker, on_delete=models.PROTECT, null=True)
    register_date = models.DateField()
    response_date = models.DateField()
    finish_date = models.DateField()


class Income(models.Model):
    user_id = models.ForeignKey(BookReaderUser, on_delete=models.PROTECT, null=True)
    amount = models.FloatField()
    date = models.DateField()
    source_financial_account_no = models.IntegerField(null=False)
    organization_financial_account = models.ForeignKey(OrganizationFinancialAccount, on_delete=models.PROTECT)


class Expense(models.Model):
    destination = models.ForeignKey(FinancialAccount)
    organization_financial_account = models.ForeignKey(OrganizationFinancialAccount, on_delete=models.PROTECT)
    amount = models.FloatField()
    date = models.DateField()


class BookPackage(models.Model):
    name = models.TextField()
    price = models.FloatField()


class BookAndBookPackage(models.Model):
    book_package_id = models.ForeignKey(BookPackage)
    book_id = models.ForeignKey(Book)

    class Meta:
        unique_together = ('book_package_id', 'book_id')


class BookComment(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey(BookReaderUser)
    book_id = models.ForeignKey(Book)
    date = models.DateField()


class CommentReply(models.Model):
    book_comment_id = models.ForeignKey(BookComment)
    user_id = models.ForeignKey(BookReaderUser)  # id of the person who wrote reply
    content = models.TextField()


class Notification(models.Model):
    content = models.TextField(null=False)
    notif_date_created = models.DateField(null=False)
    BookMaker_id = models.ForeignKey(BookMaker, null=False, on_delete=models.CASCADE)
    request_id = models.ForeignKey(TranslationRequest, null=False, on_delete=models.CASCADE)


class TranslatedBook(models.Model):
    translated_book_file = models.FileField(null=False)
    request = models.ForeignKey(TranslationRequest, null=False, on_delete=models.PROTECT)
    translator = models.ForeignKey(BookMaker, null=False, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('request', 'translator')