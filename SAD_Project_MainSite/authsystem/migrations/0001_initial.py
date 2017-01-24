# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('first_publish_year', models.IntegerField()),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('number_of_pages', models.IntegerField()),
                ('summary', models.TextField()),
                ('cover_image_addr', models.ImageField(default='Book.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='BookAndBookPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('book_comment_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookMaker',
            fields=[
                ('book_maker_id', models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female')], max_length=2)),
                ('book_maker_type', models.CharField(choices=[('TR', 'Translator'), ('AUT', 'Author'), ('Both', 'Both')], max_length=4)),
                ('avatar', models.ImageField(default='user.png', upload_to='')),
                ('telephone_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('verifier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='BookMakerLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_maker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookMaker')),
            ],
        ),
        migrations.CreateModel(
            name='BookMakerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField(null=True)),
                ('Score', models.IntegerField()),
                ('book_maker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookMaker')),
            ],
        ),
        migrations.CreateModel(
            name='BookPackage',
            fields=[
                ('package_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookReaderUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='user.png', upload_to='')),
                ('telephone_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookSeller',
            fields=[
                ('book_seller_id', models.CharField(auto_created=True, max_length=15, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(default='user.png', upload_to='')),
                ('telephone_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='BookShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('reply_comment_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('book_comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookComment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookReaderUser')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=20)),
                ('book_maker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookMaker')),
                ('book_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookSeller')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.CharField(max_length=20)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('source_financial_account_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('delivery_date', models.DateField()),
                ('order_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationFinancialAccount',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PreOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authsystem.Book')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authsystem.BookReaderUser')),
            ],
        ),
        migrations.CreateModel(
            name='SellBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('number_of_copeis', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Book')),
                ('book_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookSeller')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('shopping_cart_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookReaderUser')),
            ],
        ),
        migrations.CreateModel(
            name='TranslationRequest',
            fields=[
                ('translation_request_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('book_file', models.FileField(upload_to='')),
                ('register_date', models.DateField()),
                ('response_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('book_maker_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='authsystem.BookMaker')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authsystem.BookReaderUser')),
            ],
        ),
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Book')),
                ('book_maker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookMaker')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shopping_cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='income',
            name='organization_financial_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authsystem.OrganizationFinancialAccount'),
        ),
        migrations.AddField(
            model_name='income',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authsystem.BookReaderUser'),
        ),
        migrations.AddField(
            model_name='expense',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.FinancialAccount'),
        ),
        migrations.AddField(
            model_name='expense',
            name='organization_financial_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authsystem.OrganizationFinancialAccount'),
        ),
        migrations.AddField(
            model_name='bookshoppingcart',
            name='shopping_cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='bookrating',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookReaderUser'),
        ),
        migrations.AddField(
            model_name='bookmakerrating',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookReaderUser'),
        ),
        migrations.AddField(
            model_name='bookmakerlanguage',
            name='language_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.Language'),
        ),
        migrations.AddField(
            model_name='bookcomment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookReaderUser'),
        ),
        migrations.AddField(
            model_name='bookandbookpackage',
            name='book_package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.BookPackage'),
        ),
        migrations.AlterUniqueTogether(
            name='write',
            unique_together=set([('book_id', 'book_maker_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='sellby',
            unique_together=set([('book_id', 'book_seller_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='genre',
            unique_together=set([('genre_type', 'book_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookrating',
            unique_together=set([('book_id', 'user_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookmakerrating',
            unique_together=set([('book_maker_id', 'user_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookmakerlanguage',
            unique_together=set([('book_maker_id', 'language_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookandbookpackage',
            unique_together=set([('book_package_id', 'book_id')]),
        ),
    ]

