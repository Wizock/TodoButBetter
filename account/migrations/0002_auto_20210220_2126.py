# Generated by Django 3.1.6 on 2021-02-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsdb',
            name='Password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='accountsdb',
            name='Username',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='accountsdb',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]