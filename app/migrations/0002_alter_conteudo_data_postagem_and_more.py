# Generated by Django 5.1 on 2024-11-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='data_postagem',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_postagem',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='data_postagem',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='data_postagem',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teste',
            name='data_postagem',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
