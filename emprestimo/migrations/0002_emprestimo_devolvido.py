# Generated by Django 4.0 on 2021-12-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='devolvido',
            field=models.BooleanField(default=False),
        ),
    ]
