# Generated by Django 4.0.4 on 2022-06-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_info_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimage',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profileimage'),
        ),
    ]
