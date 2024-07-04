from django.utils.translation import gettext_lazy as _
from django.db import models


class RoleStatus(models.IntegerChoices):
    STUDENT = 1, _('Student')
    TUTOR = 2, _('Tutor')
