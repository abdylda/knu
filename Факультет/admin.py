from django.contrib import admin

from .models import Category, Edizm, NalichiTehniki, NamKabinet, Kabinet, Corps


class catigoriAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, catigoriAdmin)


class EdizmAdmin(admin.ModelAdmin):
    pass
admin.site.register(Edizm, EdizmAdmin)


class NamKabinetAdmin(admin.ModelAdmin):
    pass
admin.site.register(NamKabinet, NamKabinetAdmin)


class KabinetAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie', 'NamKabinet']
admin.site.register(Kabinet, KabinetAdmin)


class CorpsAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie']


admin.site.register(Corps, CorpsAdmin)


class NalichiTehnikiAdmin(admin.ModelAdmin):
    list_display = ['Kabinet', 'NamKabinet', 'category', 'Edizm', 'kodTMU', 'Naimenovanie', 'Kolich', 'sostoyanie']
    list_filter = ['Kabinet', 'sostoyanie', 'category', 'NamKabinet']
    search_fields = ('Kabinet', 'NamKabinet')
admin.site.register(NalichiTehniki, NalichiTehnikiAdmin)


admin.site.site_title = "Администратор сайт Абдулла"
admin.site.site_header = "Администратор сайт Абдулла"
