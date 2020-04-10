from django.db import models
from django.core import checks


class Speaker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(
        max_length=254,
        unique=True
    )
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        # Set explicit database table name to avoid
        # prefix name with the database name
        db_table = 'speakers'

    @classmethod
    def _first_name_field_warning_check(cls):
        return checks.Warning(
            (
                'Field `first_name` is deprecated and will be '
                'removed in the next version.',
             ),
            hint='Use field `full_name`.',
            obj='speaker',
            id='models.W301',
        )

    @classmethod
    def _last_name_field_warning_check(cls):
        return checks.Warning(
            (
                'Field `last_name` is deprecated and will be '
                'removed in the next version.',
             ),
            hint='Use field `full_name`.',
            obj='speaker',
            id='models.W302',
        )

    @classmethod
    def check(cls, **kwargs):
        checks = super().check(**kwargs)
        first_name_field_check = cls._first_name_field_warning_check()
        last_name_field_check = cls._last_name_field_warning_check()
        checks.extend(
            [
                first_name_field_check,
                last_name_field_check
            ]
        )

        return checks
