# Generated by Django 2.2.4 on 2020-12-15 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_dog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='img',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
