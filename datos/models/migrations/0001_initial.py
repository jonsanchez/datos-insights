# Generated by Django 2.1.7 on 2019-02-15 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datasets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_private', models.BooleanField(default=False)),
                ('cost', models.FloatField()),
                ('weights_path', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'models',
            },
        ),
        migrations.CreateModel(
            name='ModelDatasetRelations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='datasets.Dataset')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='models.Model')),
            ],
            options={
                'db_table': 'model_to_dataset',
            },
        ),
        migrations.AlterUniqueTogether(
            name='modeldatasetrelations',
            unique_together={('model', 'dataset')},
        ),
    ]
