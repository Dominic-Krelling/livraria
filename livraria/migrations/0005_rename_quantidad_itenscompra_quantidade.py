# Generated by Django 4.2.4 on 2023-09-05 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_itenscompra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itenscompra',
            old_name='quantidad',
            new_name='quantidade',
        ),
    ]