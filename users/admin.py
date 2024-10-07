from django.contrib import admin

from users.models import User
# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "username", "email", "gender", "role", "city", "country"]
