# Generated by Django 4.2.7 on 2023-11-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0009_alter_entity_options_remove_entity_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
