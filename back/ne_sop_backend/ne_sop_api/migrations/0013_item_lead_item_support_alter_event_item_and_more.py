# Generated by Django 4.2.7 on 2023-11-29 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0012_alter_event_created_alter_item_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead', to='ne_sop_api.entity'),
        ),
        migrations.AddField(
            model_name='item',
            name='support',
            field=models.ManyToManyField(related_name='support', to='ne_sop_api.entity'),
        ),
        migrations.AlterField(
            model_name='event',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ne_sop_api.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='ne_sop_api.entity'),
        ),
    ]
