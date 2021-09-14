from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'document']
admin.site.register(Document, DocumentAdmin)



admin.site.site_title = "Администратор сайт Абдулла"
admin.site.site_header = "Администратор сайт Абдулла"