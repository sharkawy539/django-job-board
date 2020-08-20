# Generated by Django 3.1 on 2020-08-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='scription',
        ),
        migrations.AddField(
            model_name='job',
            name='discription',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1, max_length=3),
        ),
    ]
