from django.contrib import admin
from django.utils.html import format_html
from .models import ReportType, Report, ReportItem, ItemType
import pprint

class ReportTypeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'detail']
    list_display = ['name', 'date_created', 'last_updated', 'preview_detail']
    fieldsets = [
        (None, {
            'fields': ['name', 'detail'],
        }),
    ]

    def preview_detail(self, obj):
        return format_html(obj.detail)

admin.site.register(ReportType, ReportTypeAdmin)

class ReportItemInline(admin.StackedInline):
    model = ReportItem
    extra = 1

class ReportAdmin(admin.ModelAdmin):
    inlines = [ReportItemInline]
    search_fields = ['name', 'date_from', 'date_to', 'detail']
    list_display = ['name', 'date_created', 'last_updated', 'date_from', 'date_to', 'preview_detail']
    
    fieldsets = [
        ('DATE RANGE', {
            'fields': ['date_from', 'date_to'],
        }),
        ('REPORT DETAIL', {
            'fields': ['report_type', 'name', 'detail'],
        }),
        (
         'REPORT PREVIEW', {
             'fields': ['preview_report']
        }),
    ]
    readonly_fields = ['preview_report']

    def preview_detail(self, obj):
        return format_html(obj.detail)

    preview_detail.short_description = 'detail'
    preview_detail.admin_order_field = 'detail'

    def preview_report(self, obj):
        return format_html('''
            {}
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Value</th>
                    </tr>
                </thead>
            </table>
        '''.format((obj.report_item.all())))

    preview_report.short_description = 'Preview Report'

admin.site.register(Report, ReportAdmin)

class ItemTypeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'detail']
    list_display = ['name', 'date_created', 'last_updated', 'preview_detail']

    def preview_detail(self, obj):
        return format_html(obj.detail)

    preview_detail.short_description = 'detail'
    preview_detail.admin_order_field = 'detail'

admin.site.register(ItemType, ItemTypeAdmin)
