from django.core.validators import MaxValueValidator
from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    return "tutors/photos/user_{id}/{file}".format(id=instance.user.id, file=filename)


class Tutor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tutor')
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name=_('Photo'))
    city = models.CharField(max_length=25, null=False, blank=False, verbose_name=_('City'))
    address = models.CharField(max_length=250, null=False, blank=False, verbose_name=_('Address'))
    subject = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Subject'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    month_price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                      blank=False, verbose_name=_('Monthly Price'))

    class Meta:
        verbose_name = _('Tutor')
        verbose_name_plural = _('Tutors')

    @property
    def average_rating(self):
        return Review.objects.filter(tutor=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f'{self.user}'


class Review(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='review')
    rating = models.PositiveSmallIntegerField(null=False, blank=False, validators=[MaxValueValidator(5)],
                                              verbose_name=_('Rating'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        unique_together = ('tutor', 'student')
