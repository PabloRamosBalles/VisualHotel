from django.contrib import admin
from applications.users.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_filter = ['hotel']

admin.site.register(User, UserAdmin)