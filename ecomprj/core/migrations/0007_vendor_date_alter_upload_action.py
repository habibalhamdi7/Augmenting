# Generated by Django 4.1.4 on 2023-05-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_upload_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert'), ('SHARPEN', 'sharpen'), ('MEDIAN', 'median'), ('NOISE_REDUCTION', 'noise reduction'), ('BILATERAL', 'bilateral')], max_length=50),
        ),
    ]