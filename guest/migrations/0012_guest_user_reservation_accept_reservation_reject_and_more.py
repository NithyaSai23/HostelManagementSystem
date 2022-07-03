# Generated by Django 4.0.5 on 2022-07-03 12:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guest', '0011_reservation_room_alloted'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reject',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='first_name',
            field=models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='guest',
            name='last_name',
            field=models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='room',
            name='max_persons',
            field=models.IntegerField(default=2),
        ),
    ]
