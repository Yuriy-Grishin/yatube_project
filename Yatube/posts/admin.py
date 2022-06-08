from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') 
    list_editable = ('group',)
    search_fields = ('text',) 
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

admin.site.register(Post)

from .models import Group

class GroupAdmin(admin.ModelAdmin):
    
    title = ('pk', 'text') 
    slug = ('text',) 
    description = ('pub_date',)
    
    empty_value_display = '-пусто-'

admin.site.register(Group)