# Generated by Django 4.0.3 on 2022-04-09 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_auction_app', '0004_delete_userinformation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useremails',
            old_name='userId',
            new_name='id',
        ),
    ]
