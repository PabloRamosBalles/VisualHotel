from django.contrib import admin
from applications.room.models import Room
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_filter = ['hotel']

admin.site.register(Room, RoomAdmin)