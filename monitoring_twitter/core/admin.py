from django.contrib import admin
from core.models import RequestAPI


class RequestAPIAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('total_request', 'date')
    model = RequestAPI


admin.site.register(RequestAPI, RequestAPIAdmin)
