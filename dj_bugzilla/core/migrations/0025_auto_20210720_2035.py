# Generated by Django 3.1.6 on 2021-07-21 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210713_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField()),
                ('notification_is_seen', models.BooleanField(default=False)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('admin_role_assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.administrator')),
                ('dev_role_assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.developer')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_from', to=settings.AUTH_USER_MODEL)),
                ('pm_role_assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.projectmanager')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.task')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.ticket')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
