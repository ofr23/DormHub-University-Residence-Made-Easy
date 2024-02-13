# Generated by Django 4.1.1 on 2024-02-13 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Provost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminId', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallId', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('hallAdmin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hall_Admin.halladmin')),
                ('provost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Provost.provost')),
            ],
        ),
    ]