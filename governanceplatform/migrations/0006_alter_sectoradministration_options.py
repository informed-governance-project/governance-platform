# Generated by Django 4.2.1 on 2023-05-31 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "governanceplatform",
            "0005_alter_company_email_alter_company_phone_number_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sectoradministration",
            options={
                "verbose_name": "Sector administration",
                "verbose_name_plural": "Sectors administration",
            },
        ),
    ]
