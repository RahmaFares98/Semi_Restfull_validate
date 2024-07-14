from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_release_date_in_past(value):
    today = timezone.now().date()
    if value > today:
        raise ValidationError('Release date must be in the past.')

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    release_date = models.DateField(validators=[validate_release_date_in_past])
    description = models.TextField(blank=True)

    def clean(self):
        # Optional description should have at least 10 characters
        if self.description and len(self.description) < 10:
            raise ValidationError('Description must be at least 10 characters long.')

    def __str__(self):
        return self.title
