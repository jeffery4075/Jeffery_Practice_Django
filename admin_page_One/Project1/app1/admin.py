from django.contrib import admin
from .models import Profile_Details , student_Details

class Profile_DetailsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'roll')
    search_fields = ('Name', 'Email')

admin.site.register(Profile_Details,Profile_DetailsAdmin)
admin.site.register(student_Details)
