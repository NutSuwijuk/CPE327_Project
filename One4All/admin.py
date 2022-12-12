from django.contrib import admin

from One4All.models import Video
from One4All.models import Person

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "image"]
    search_fields = ["title"]
admin.site.register(Video, VideoAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ["no", "title", "link", "image"]
    search_fields = ["title"]
admin.site.register(Person, PersonAdmin)