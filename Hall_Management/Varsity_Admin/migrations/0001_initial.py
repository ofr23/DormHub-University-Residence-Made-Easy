# Generated by Django 4.1.1 on 2024-02-24 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Provost', '0001_initial'),
        ('Hall_Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallId', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('hallAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hall_Admin.halladmin')),
                ('provost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Provost.provost')),
            ],
        ),
        migrations.CreateModel(
            name='VarsityAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('username', models.CharField(default='NOne', max_length=100)),
                ('password', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.IntegerField(blank=True, default=0, null=True)),
                ('capacity', models.IntegerField(blank=True, default=0, null=True)),
                ('color', models.CharField(blank=True, max_length=70, null=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Varsity_Admin.hall')),
            ],
        ),
    ]
