from django.contrib import admin
from .models import Note, Tag

# Register your models here.

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'timestamp']

    class Meta:
        model = Note

class TagModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag


admin.site.register(Note, NoteModelAdmin)    
admin.site.register(Tag, TagModelAdmin)    