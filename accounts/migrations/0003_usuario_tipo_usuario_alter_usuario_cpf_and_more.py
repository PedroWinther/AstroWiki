# Generated by Django 5.1 on 2024-11-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usuario_escolaridade'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('aluno', 'Aluno'), ('autor', 'Autor'), ('administrador', 'Administrador')], default='aluno', max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome_completo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
