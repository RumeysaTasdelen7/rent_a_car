# Generated by Django 4.2.5 on 2023-10-06 18:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pickUpTime",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 10, 6, 18, 25, 4, 45986, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "dropOffTime",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 10, 6, 18, 25, 4, 45986, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("pickUpLocation", models.CharField(max_length=150)),
                ("dropOffLocation", models.CharField(max_length=150)),
                ("status", models.CharField(default="CREATED", max_length=20)),
                ("totalPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cars.car"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]