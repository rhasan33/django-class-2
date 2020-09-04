from django.db import models
from django.contrib.postgres.fields import JSONField


class Restaurant(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'active'
        INACTIVE = 'inactive', 'inactive'

    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=180, unique=True)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.INACTIVE)
    meta = JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return self.name
