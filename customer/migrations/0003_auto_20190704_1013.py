# Generated by Django 2.2.3 on 2019-07-04 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190704_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='type',
            new_name='designation',
        ),
    ]