# Generated by Django 3.0.6 on 2020-05-10 05:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursinary_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursinary_app.Subject')),
            ],
            options={
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursinary_app.Course')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
