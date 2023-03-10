from django.contrib import admin
from users.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class user_profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'language', 'phone_number', 'occupation', 'description', 'availability', 'birth_date', 'years_of_experience', 'address', 'company_name', 'profile_image', 'cover_image',)