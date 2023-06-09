# Generated by Django 4.2.2 on 2023-07-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("governanceplatform", "0003_sectorcontact_unique_sectorcontact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="companies",
            field=models.ManyToManyField(
                related_name="users",
                through="governanceplatform.CompanyAdministrator",
                to="governanceplatform.company",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="sectors",
            field=models.ManyToManyField(
                related_name="users",
                through="governanceplatform.SectorContact",
                to="governanceplatform.sector",
            ),
        ),
    ]
