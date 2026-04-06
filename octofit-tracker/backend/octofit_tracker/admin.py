from django.contrib import admin
from .models import CustomUser, Team, Activity, Workout, Leaderboard
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('team',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('team',)}),
    )
    list_display = ('username', 'email', 'team', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
