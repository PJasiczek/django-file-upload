# Generated by Django 4.0.4 on 2022-05-29 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Identyfikator wyceny')),
                ('first_name', models.CharField(max_length=255, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=255, verbose_name='Nazwisko')),
                ('email_address', models.EmailField(max_length=255, verbose_name='Adres email')),
                ('telephone_number', models.CharField(blank=True, max_length=255, verbose_name='Numer telefonu')),
                ('description', models.TextField(blank=True, verbose_name='Opis')),
                ('was_realized', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Zamówienie',
                'verbose_name_plural': 'Zamówienia',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to='documents/', verbose_name='Plik')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='upload_app.order', verbose_name='Identyfikator wyceny')),
            ],
            options={
                'verbose_name': 'Plik',
                'verbose_name_plural': 'Pliki',
            },
        ),
    ]
