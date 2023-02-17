# Generated by Django 4.1.5 on 2023-02-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essivivi_api', '0002_remove_produit_volume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eau',
            name='imageUrl',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='eau',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]