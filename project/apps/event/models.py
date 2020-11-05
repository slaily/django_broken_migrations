from django.db import models

from project.apps.speaker.models import Speaker


class Event(models.Model):
    title = models.CharField(max_length=254)
    speaker = models.ForeignKey(
        Speaker,
        related_name='events',
        on_delete=models.CASCADE
    )

    class Meta:
        # Set explicit database table name to avoid
        # prefix name with the database name
        db_table = 'events'
