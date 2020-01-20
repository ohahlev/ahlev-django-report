from django.db import models
from tinymce.models import HTMLField
#from vehicle.models.vehicle import Vehicle

class ReportType(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    detail = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Report Type'
        db_table = 'report_type'

    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    date_from = models.DateTimeField(verbose_name='from')
    date_to = models.DateTimeField(verbose_name='to')
    detail = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE, verbose_name='Report Type')
    #vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehicle')

    class Meta:
        verbose_name = 'Report'

    def __str__(self):
        return self.name

class ItemType(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=True)
    detail = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item Type'
        db_table = 'item_type'
    
    def __str__(self):
        return self.name if self.name else self.id

class ReportItem(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=True)
    value = models.FloatField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, verbose_name='Item Type')
    report = models.ForeignKey(Report, on_delete=models.CASCADE, verbose_name='Report')

    class Meta:
        verbose_name = 'Report Item'
        db_table = 'report_item'

    def __str__(self):
        return self.name



