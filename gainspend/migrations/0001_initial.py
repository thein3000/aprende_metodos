# Generated by Django 2.1.2 on 2018-11-11 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('field_id', models.IntegerField(blank=True, db_column='_id', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('is_subject', models.BooleanField(blank=True, null=True)),
                ('preface_name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMethod',
            fields=[
                ('field_id', models.IntegerField(blank=True, db_column='_id', primary_key=True, serialize=False)),
                ('completed', models.BooleanField(blank=True, null=True)),
                ('paramaters', models.TextField(blank=True, null=True)),
                ('method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gainspend.Method')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
