# Generated by Django 3.2.16 on 2022-10-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/128/1159/1159207.png?ga=GA1.2.729369652.1666116741', max_length=500),
        ),
    ]
