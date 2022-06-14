# Generated by Django 4.0.5 on 2022-06-14 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m2', models.CharField(max_length=3)),
                ('m3', models.CharField(max_length=3)),
                ('mt', models.CharField(max_length=3)),
                ('kg', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='İscilik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rayic', models.CharField(max_length=15)),
                ('is_tanım', models.CharField(max_length=100)),
                ('is_miktar', models.DecimalField(decimal_places=3, max_digits=5)),
                ('is_fiyat', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Makine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mak_rayic', models.CharField(max_length=15)),
                ('mak_tanım', models.CharField(max_length=100)),
                ('mak_miktar', models.DecimalField(decimal_places=3, max_digits=5)),
                ('mak_fiyat', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Malzeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal_rayic', models.CharField(max_length=15)),
                ('mal_tanım', models.CharField(max_length=100)),
                ('mal_miktar', models.DecimalField(decimal_places=3, max_digits=5)),
                ('mal_fiyat', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='BirimFiyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poz_no', models.CharField(max_length=15)),
                ('tanım', models.CharField(max_length=100)),
                ('fiyat', models.DecimalField(decimal_places=3, max_digits=10)),
                ('slug', models.SlugField(unique=True)),
                ('birim_fiyat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pmuyg.birim')),
                ('iscilik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmuyg.i̇scilik')),
                ('makine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmuyg.makine')),
                ('malzeme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmuyg.malzeme')),
            ],
        ),
    ]