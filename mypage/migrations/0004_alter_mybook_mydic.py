# Generated by Django 4.1.1 on 2022-11-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0003_alter_mybook_mydic_alter_mybook_mylike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybook',
            name='mydic',
            field=models.IntegerField(null=True),
        ),
    ]
