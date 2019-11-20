from django.contrib import admin
from member.models import MemTable

# Register your models here.
class MemTableAdmin(admin.ModelAdmin):
    list_display = ('id','memid','passwd','name','email','phone','zipcode','address','job')
    
admin.site.register(MemTable, MemTableAdmin)