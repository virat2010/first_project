# Generated by Django 3.2.5 on 2022-08-07 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfoForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='first_app.user')),
            ],
        ),
    ]