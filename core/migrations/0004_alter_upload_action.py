# Generated by Django 4.1.4 on 2023-05-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert'), ('DEBLURRED', 'deblurred')], max_length=50),
        ),
    ]
