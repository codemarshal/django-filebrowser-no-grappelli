import sys
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FileBrowser(models.Model):
    class Meta:
        managed = sys.argv[1:2] == ['test']
        verbose_name = _("FileBrowser")
        verbose_name_plural = _("FileBrowser")
