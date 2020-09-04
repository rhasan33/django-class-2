# Generated by Django 3.1 on 2020-09-04 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('address', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('is_active', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='inactive', max_length=10)),
                ('meta', models.JSONField(default=dict)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]