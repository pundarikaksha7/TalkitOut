# Generated by Django 4.1.3 on 2022-12-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="votes", field=models.IntegerField(default=0),
        ),
    ]
