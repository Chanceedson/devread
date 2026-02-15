from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

fields = UserAdmin.fieldsets + (
    ('Tech Profile', {'fields': ('avatar', 'bio', 'github_username', 'website','primary_techstack')}),
)

class CustomUserAdmin(UserAdmin):
    fieldsets = fields

admin.site.register(User, CustomUserAdmin)

# Register your models here.
