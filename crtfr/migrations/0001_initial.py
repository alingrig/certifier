# Generated by Django 2.1.7 on 2019-03-18 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PixelProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RunReconstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reconstruction', models.CharField(choices=[('online', 'Online'), ('express', 'Express'), ('prompt', 'Prompt'), ('rereco', 'ReReco')], max_length=8)),
                ('dataset', models.CharField(max_length=150)),
                ('is_reference', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StripProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TrackingProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TrackerCertification',
            fields=[
                ('runreconstruction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='crtfr.RunReconstruction')),
                ('pixel', models.CharField(choices=[('bad', 'Bad'), ('good', 'Good'), ('excluded', 'Excluded')], max_length=3)),
                ('strip', models.CharField(choices=[('bad', 'Bad'), ('good', 'Good'), ('excluded', 'Excluded')], max_length=3)),
                ('tracking', models.CharField(choices=[('bad', 'Bad'), ('good', 'Good'), ('excluded', 'Excluded')], max_length=3)),
                ('pixel_lowstat', models.BooleanField(default=False)),
                ('strip_lowstat', models.BooleanField(default=False)),
                ('tracking_lowstat', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('bad_reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crtfr.BadReason')),
                ('pixel_problems', models.ManyToManyField(blank=True, to='crtfr.PixelProblem')),
            ],
        ),
        migrations.AddField(
            model_name='runreconstruction',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.OmsRun'),
        ),
        migrations.AddField(
            model_name='trackercertification',
            name='reference_runreconstruction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='crtfr.RunReconstruction'),
        ),
        migrations.AddField(
            model_name='trackercertification',
            name='strip_problems',
            field=models.ManyToManyField(blank=True, to='crtfr.StripProblem'),
        ),
        migrations.AddField(
            model_name='trackercertification',
            name='tracking_problems',
            field=models.ManyToManyField(blank=True, to='crtfr.TrackingProblem'),
        ),
        migrations.AlterUniqueTogether(
            name='runreconstruction',
            unique_together={('run', 'reconstruction')},
        ),
    ]
