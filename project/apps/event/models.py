from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=254)

    class Meta:
        # Set explicit database table name to avoid
        # prefix name with the database name
        db_table = 'events'
