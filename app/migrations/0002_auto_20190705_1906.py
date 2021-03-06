# Generated by Django 2.2.3 on 2019-07-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=15)),
                ('mensagem', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='nome_medico',
            new_name='nome_Medico',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='crm',
        ),
        migrations.AddField(
            model_name='medico',
            name='CEP',
            field=models.CharField(default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='CRM',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='email',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='telefone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medico',
            name='regiao',
            field=models.CharField(choices=[('Z1', 'Zona Norte'), ('Z2', 'Zona Sul'), ('Z3', 'Zona Leste'), ('Z4', 'Zona Oeste'), ('Z5', 'Centro')], max_length=20),
        ),
    ]
