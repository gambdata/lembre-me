from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import Usuario

class UserAdminConfig(UserAdmin):
    model = Usuario
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ['email', 'username', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permissão', {'fields': ('is_active', 'is_staff')}),
        ('Pessoal', {'fields': ('about',)})
    )
    formfield_overrides = {
        Usuario.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )

admin.site.register(Usuario, UserAdminConfig)
