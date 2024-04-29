from django.contrib import admin
from .models import *

# Register your models here.

class HaberAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','author','published_date','updated_date')
    list_filter = ('published_date','updated_date')
    date_hierarchy = 'published_date'
    
    actions = ['delete_selected']



admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Haber)



