from django.contrib import admin
from .models import User,Diseases

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
     list_display = ('id', 'username', 'email', 'password')

admin.site.register(Diseases)

