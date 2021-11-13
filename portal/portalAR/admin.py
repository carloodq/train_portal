from django.contrib import admin
from .models import scena, componente, stabile, manutenzione
from django.utils.html import format_html


class admin_scena(admin.ModelAdmin):
    search_fields = ("stabile",)
    list_display = ("id", "stabile", "scena", "tipo_di_impianto")
    list_filter = ["stabile", "scena"]

class admin_componente(admin.ModelAdmin):
    list_display = ("id", "scena", "codice", "modello", "show_firm_url", "data_aggiunta")
    list_filter = ["scena"]
    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

class admin_stabile(admin.ModelAdmin):
    list_display = ("id", "facility_manager", "nome_stabile", "indirizzo")
    list_filter = ["facility_manager"]

class admin_manutenzione(admin.ModelAdmin):
    list_display = ("id", "scena", "manutentore", "è_richiesta_iniziale")
    list_filter = ["manutentore", "scena"]

# Register your models here.
admin.site.register(scena, admin_scena)
admin.site.register(componente, admin_componente)
admin.site.register(stabile, admin_stabile)
admin.site.register(manutenzione, admin_manutenzione)