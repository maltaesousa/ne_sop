# Generated by Django 4.2.7 on 2023-11-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0010_entity_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='content',
            field=models.TextField(blank=True, default='', max_length=600),
        ),
        migrations.AddField(
            model_name='item',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entity',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
