# Generated by Django 2.1.7 on 2019-02-25 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0002_auto_20190216_0922'),
        ('models', '0002_auto_20190216_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='datasets',
            field=models.ManyToManyField(through='models.ModelDatasetRelations', to='datasets.Dataset'),
        ),
        migrations.AddField(
            model_name='modeldatasetrelations',
            name='date_related',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
