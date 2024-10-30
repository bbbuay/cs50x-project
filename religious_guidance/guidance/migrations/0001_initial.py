# Generated by Django 5.1.2 on 2024-10-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guidance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='guidance_images/')),
                ('religion', models.CharField(choices=[('B', 'Buddhism'), ('C', 'Christianity')], max_length=1)),
                ('favorite_users', models.ManyToManyField(related_name='favorite_guidances', to='user.userprofile')),
            ],
        ),
    ]