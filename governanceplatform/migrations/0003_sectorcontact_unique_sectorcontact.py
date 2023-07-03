# Generated by Django 4.2.2 on 2023-06-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("governanceplatform", "0002_company_types_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="sectorcontact",
            constraint=models.UniqueConstraint(
                fields=("user", "sector"), name="unique_SectorContact"
            ),
        ),
    ]