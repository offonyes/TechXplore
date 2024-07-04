# Generated by Django 5.0.6 on 2024-07-04 06:22

import django.core.validators
import django.db.models.deletion
import tutor_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=tutor_app.models.user_directory_path, verbose_name='Photo')),
                ('city', models.CharField(max_length=25, verbose_name='City')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('experience', models.IntegerField(verbose_name='Experience')),
                ('month_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Monthly Price')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutors',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='tutor_app.tutor')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'unique_together': {('tutor', 'student')},
            },
        ),
    ]
