from django.apps import AppConfig
from . import __version__ as VERSION

class ReportConfig(AppConfig):
    name = "report"
    verbose_name = "Report Management %s" % VERSION
