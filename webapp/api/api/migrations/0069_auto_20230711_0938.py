# Generated by Django 2.2.28 on 2023-07-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_auto_20230203_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='annotation_classification',
            field=models.BooleanField(default=False, help_text='If these project annotations are suitablefor training a general purpose model. Ifin doubt mark this as False.'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('A', 'Annotating'), ('D', 'Discontinued (Fail)'), ('C', 'Complete')], default='A', help_text='The status of the project to indicate the readiness', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='projected_locked',
            field=models.BooleanField(default=False, help_text='If this project is locked and cannot or should not be touched any further.'),
        ),
    ]