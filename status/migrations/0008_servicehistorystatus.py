# Generated by Django 2.0.5 on 2020-01-07 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0007_auto_20200107_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHistoryStatus',
            fields=[
                ('service_history_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField()),
                ('service_history', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.ServicesHistory')),
                ('service_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.ServicesStatus')),
            ],
        ),
    ]