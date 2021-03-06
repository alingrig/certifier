# Generated by Django 2.1.7 on 2019-10-24 07:44

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
            name='OpenRuns',
            fields=[
                ('run_number', models.PositiveIntegerField(help_text='Run number', primary_key=True, serialize=False, verbose_name='Run')),
                ('dataset_express', models.CharField(max_length=150)),
                ('dataset_prompt', models.CharField(blank=True, max_length=150, null=True)),
                ('dataset_rereco', models.CharField(blank=True, max_length=150, null=True)),
                ('dataset_rereco_ul', models.CharField(blank=True, max_length=150, null=True)),
                ('date_retrieved', models.DateField()),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
