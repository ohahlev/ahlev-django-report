from django.apps import AppConfig
from django.utils.html import format_html
from . import __version__ as VERSION

class ReportConfig(AppConfig):
    name = 'report'
    verbose_name = format_html("Report Management {}", VERSION)
