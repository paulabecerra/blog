# Generated by Django 2.2.4 on 2019-09-04 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='work/photos'),
        ),
    ]
