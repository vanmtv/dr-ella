# Generated by Django 2.2.3 on 2019-07-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190705_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='medico',
            name='CEP',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='medico',
            name='CRM',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='medico',
            name='endereco',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='medico',
            name='nome_Medico',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='medico',
            name='regiao',
            field=models.CharField(choices=[('Z1', 'Zona Norte'), ('Z2', 'Zona Sul'), ('Z3', 'Zona Leste'), ('Z4', 'Zona Oeste'), ('Z5', 'Centro')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
