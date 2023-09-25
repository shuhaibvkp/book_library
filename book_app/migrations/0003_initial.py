# Generated by Django 4.2.1 on 2023-07-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_app', '0002_delete_regmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='addbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boname', models.CharField(max_length=30)),
                ('auname', models.CharField(max_length=30)),
                ('bopdf', models.FileField(upload_to='book_app/static')),
                ('boimage', models.FileField(upload_to='book_app/static')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]