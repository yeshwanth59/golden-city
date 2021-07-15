from django.contrib import admin
from goldencityApp.models import User, Master

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "first_name", "last_name", "mobile", "email", "dob"]
                    
                    
class MasterAdmin(admin.ModelAdmin):
    list_display = ["thumbnails"]


admin.site.register(User, UserAdmin)
admin.site.register(Master, MasterAdmin)