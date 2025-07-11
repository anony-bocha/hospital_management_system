# Generated by Django 5.2 on 2025-07-09 09:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0002_alter_appointment_options_alter_doctor_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appointment",
            options={
                "ordering": ["-date", "-time"],
                "verbose_name": "Appointment",
                "verbose_name_plural": "Appointments",
            },
        ),
        migrations.AlterModelOptions(
            name="doctor",
            options={
                "ordering": ["name"],
                "verbose_name": "Doctor",
                "verbose_name_plural": "Doctors",
            },
        ),
        migrations.AlterModelOptions(
            name="patient",
            options={
                "ordering": ["name"],
                "verbose_name": "Patient",
                "verbose_name_plural": "Patients",
            },
        ),
        migrations.RenameField(
            model_name="doctor",
            old_name="mobile",
            new_name="phone",
        ),
        migrations.AddField(
            model_name="appointment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="address",
            field=models.TextField(default="Not Provided"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doctor",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doctor",
            name="email",
            field=models.EmailField(
                default="Not Provided", max_length=254, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doctor",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default=1, max_length=1
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doctor",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="specialization",
            field=models.CharField(max_length=100),
        ),
    ]
