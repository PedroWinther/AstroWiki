# Generated by Django 5.1.2 on 2024-11-01 21:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NivelDificuldade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_dificuldade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_postagem', models.DateField(default=None)),
                ('titulo', models.CharField(default=None, max_length=50)),
                ('descricao', models.CharField(default=None, max_length=300)),
                ('conteudo', models.TextField()),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComentarioConteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('conteudo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.conteudo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=None, max_length=50)),
                ('nivel_ensino', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.nivelensino')),
                ('nivel_dificuldade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.niveldificuldade')),
            ],
        ),
        migrations.AddField(
            model_name='conteudo',
            name='materia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.materia'),
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_postagem', models.DateField(default=None)),
                ('titulo', models.CharField(default=None, max_length=50)),
                ('descricao', models.CharField(default=None, max_length=300)),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('conteudos', models.ManyToManyField(to='app.conteudo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_postagem', models.DateField(default=None)),
                ('titulo', models.CharField(default=None, max_length=50)),
                ('descricao', models.CharField(default=None, max_length=300)),
                ('area', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.area')),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('modulos', models.ManyToManyField(to='app.modulo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_postagem', models.DateField(default=None)),
                ('titulo', models.CharField(default=None, max_length=50)),
                ('enunciado', models.TextField()),
                ('alternativas', models.TextField()),
                ('resposta', models.CharField(max_length=500)),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
                ('nivel_dificuldade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.niveldificuldade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('area', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.AddField(
            model_name='modulo',
            name='subarea',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.subarea'),
        ),
        migrations.AddField(
            model_name='materia',
            name='subarea',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.subarea'),
        ),
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_postagem', models.DateField(default=None)),
                ('titulo', models.CharField(default=None, max_length=50)),
                ('descricao', models.CharField(default=None, max_length=300)),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('materia', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
                ('nivel_dificuldade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.niveldificuldade')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]