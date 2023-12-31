# Generated by Django 4.1.7 on 2023-04-14 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crystal_admin", "0005_alter_agent_commission_user_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event_details",
            name="manager_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="crystal_admin.manager",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="manager_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="crystal_admin.manager",
            ),
        ),
    ]
