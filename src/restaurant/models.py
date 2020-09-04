from uuid import uuid4

from django.db import models

from base.models import BaseModel


class Restaurant(BaseModel):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'active'
        INACTIVE = 'inactive', 'inactive'

    name = models.CharField(max_length=150)
    slug = models.UUIDField(editable=False, default=uuid4, unique=True)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.INACTIVE)
    meta = models.JSONField(default=dict)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return self.name
