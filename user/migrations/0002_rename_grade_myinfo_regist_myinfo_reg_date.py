# Generated by Django 4.1.1 on 2023-03-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="myinfo",
            old_name="grade",
            new_name="regist",
        ),
        migrations.AddField(
            model_name="myinfo",
            name="reg_date",
            field=models.DateTimeField(null=True),
        ),
    ]
