# Generated by Django 4.0 on 2021-12-24 11:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usuario_telefone'),
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Genero',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.usuario')),
            ],
            options={
                'verbose_name': 'Emprestimo',
            },
        ),
        migrations.AddField(
            model_name='livros',
            name='genero',
            field=models.ForeignKey(default='88888888', on_delete=django.db.models.deletion.DO_NOTHING, to='livro.genero'),
            preserve_default=False,
        ),
    ]
