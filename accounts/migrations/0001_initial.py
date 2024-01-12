# Generated by Django 4.2.6 on 2024-01-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_photo', models.ImageField(upload_to='accounts/images')),
                ('shipping_address', models.TextField()),
            ],
        ),
    ]
