# Generated by Django 2.0.2 on 2018-02-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busline',
            name='line_index',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]