# Generated by Django 5.1 on 2024-11-04 01:45

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_usuario_comentarioconteudo_autor_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarioconteudo',
            name='comentario_pai',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='app.comentarioconteudo'),
        ),
        migrations.AddField(
            model_name='comentarioconteudo',
            name='data_comentario',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentarioconteudo',
            name='autor',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentarioconteudo',
            name='comentario',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comentarioconteudo',
            name='conteudo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conteudo'),
        ),
        migrations.CreateModel(
            name='ComentarioCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comentario_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='app.comentariocurso')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComentarioModulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comentario_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='app.comentariomodulo')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.modulo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComentarioQuestao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comentario_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='app.comentarioquestao')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComentarioTeste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comentario_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='app.comentarioteste')),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teste')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
