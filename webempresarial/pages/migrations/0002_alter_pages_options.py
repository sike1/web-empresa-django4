# Generated by Django 4.2 on 2023-04-12 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
    ]
