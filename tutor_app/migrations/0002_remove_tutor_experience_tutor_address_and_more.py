# Generated by Django 5.0.6 on 2024-07-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='experience',
        ),
        migrations.AddField(
            model_name='tutor',
            name='address',
            field=models.CharField(default=1, max_length=250, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
    ]
