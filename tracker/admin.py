from django.contrib import admin
from tracker.models import Issue, Status, Type


class IssueAdmin(admin.ModelAdmin):
    list_display = ('summary', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'type')
    search_fields = ('summary', 'description')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
