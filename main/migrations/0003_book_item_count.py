# Generated by Django 4.0.5 on 2022-06-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_booktitle_book_list_db_name_book_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_item',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]