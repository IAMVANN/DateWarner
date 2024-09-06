# Generated by Django 4.2.10 on 2024-03-18 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myASD', '0002_alter_submission_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='admin_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='new', max_length=20),
        ),
    ]
