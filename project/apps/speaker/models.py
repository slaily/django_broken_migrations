from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        # Set explicit database table name to avoid
        # prefix name with the database name
        db_table = 'speakers'
