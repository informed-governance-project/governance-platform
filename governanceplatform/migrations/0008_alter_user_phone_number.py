# Generated by Django 4.2.1 on 2023-05-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("governanceplatform", "0007_alter_sector_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
    ]
