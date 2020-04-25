# Generated by Django 2.2.8 on 2020-04-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title'], name='idx_book_name'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['publication_year'], name='idx_book_publication_year'),
        ),
    ]
