# Generated by Django 4.0.2 on 2022-02-06 23:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('describe', models.TextField(blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.category_type')),
            ],
        ),
    ]