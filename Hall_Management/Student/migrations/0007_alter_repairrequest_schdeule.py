# Generated by Django 4.1.1 on 2024-02-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_alter_repairrequest_schdeule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairrequest',
            name='schdeule',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
