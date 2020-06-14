# Generated by Django 3.0.7 on 2020-06-13 00:02

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_remove_vendor_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(default=1, max_length=18, unique=True),
            preserve_default=False,
        ),
    ]
