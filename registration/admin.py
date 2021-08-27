from django.contrib import admin
from registration.models import Professional
# Register your models here.

class ProfessionalAdmin(admin.ModelAdmin):
    search_fields= ["last_name", "first_name", "other_name", "email"]
    list_display= ["last_name", "first_name", "other_name", "gender", "approved"]
    list_display_links= ["last_name", "first_name", "other_name", "gender", "approved"]
    list_filter= ["approved"]

admin.site.register(Professional, ProfessionalAdmin)
