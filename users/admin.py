from django.contrib import admin
from users.models import UserProfileInfo, Slide, Welcome, Announcement, Event
from django.db import models
from django.utils.html import format_html
from urllib import request


class UserProfileInfoAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.user))

    thumbnail.short_description = 'ProfilePic'    
    list_display = ["id", "thumbnail", "user_type", "user", "role"]
    list_display_links = ('id', "thumbnail", "user", "role" )
    search_fields = ("id", "user","role" )
    list_filter = ("role", "user", "user_type")
    formfield_overrides = {
    }


class SlideAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Slide Icon'    
    list_display = ["id", "thumbnail", "title", "image"]
    list_display_links = ('id', "thumbnail", "title", "image" )
    search_fields = ("id", "title" )
    formfield_overrides = {
    }

class AnnouncementAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Notice Icon'    
    list_display = ["id", "thumbnail", "subject", "image"]
    list_display_links = ('id', "thumbnail", "subject", "image" )
    search_fields = ("id", "subject" )
    formfield_overrides = {
    }

class EventAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Event Icon'    
    list_display = ["id", "thumbnail", "subject", "image"]
    list_display_links = ('id', "thumbnail", "subject", "image" )
    search_fields = ("id", "subject" )
    formfield_overrides = {
    }


admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Welcome)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Event, EventAdmin)


