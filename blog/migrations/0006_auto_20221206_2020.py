# Generated by Django 3.2.9 on 2022-12-06 14:50

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_announcements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='announce',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
