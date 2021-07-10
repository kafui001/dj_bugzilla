# Generated by Django 3.1.6 on 2021-07-10 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210710_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_comment', to='core.ticket'),
        ),
    ]
