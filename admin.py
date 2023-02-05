from django.contrib import admin
from .models import URegister,Zip,Upload
# Register your models here.
class URegisterAdmin(admin.ModelAdmin):
    list_display=('name','email','passwordHash')
class ZipAdmin(admin.ModelAdmin):
    list_display=('ngoname','zipcode','email','contactNumber','password','address')
class UploadAdmin(admin.ModelAdmin):
    list_display=('ngoname','ngoemail','uname','umobile','uemail','uaddress','umessage','ustatus')
admin.site.register(URegister,URegisterAdmin)
admin.site.register(Zip,ZipAdmin)
admin.site.register(Upload,UploadAdmin)