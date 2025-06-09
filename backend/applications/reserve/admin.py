from django.contrib import admin
from applications.reserve.models import Reserve
# Register your models here.
class ReserveAdmin(admin.ModelAdmin):
    list_filter = ['hotel']

admin.site.register(Reserve, ReserveAdmin)