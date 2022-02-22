from django.contrib import admin
from school.models import Grade, Subject, Lesson, Comment, Reply, WorkingDays, TimeSlots, SlotSubject
from django.db import models
from django.utils.html import format_html
from embed_video.admin import AdminVideoMixin


class GradeAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Garde Icon'    
    list_display = ["id", "thumbnail", "name", "slug", "image"]
    list_display_links = ('id', "thumbnail", "name", )
    search_fields = ('id', "name", )
    list_filter = ("name", )
    formfield_overrides = {
    
    }


class SubjectAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Subject Icon'    
    list_display = ["id", "thumbnail", "name", "slug", "image", "grade" ]
    list_display_links = ('id', "thumbnail", "name",  "grade" )
    search_fields = ('id', "name", "grade" )
    list_filter = ("name", "grade" )
    formfield_overrides = {
   
    }


class LessonAdmin(AdminVideoMixin, admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.name))

    thumbnail.short_description = 'Lesson Icon'    
    list_display = ["lesson_id", "thumbnail", "name", "created_by", "created_at", "subject" ]
    list_display_links = ("lesson_id", "thumbnail", "name", "subject" )
    search_fields = ('lesson_id', "name", "grade", "created_by", "created_at", "subject" )
    list_filter = ("name", "created_by", "created_at", "subject" )
    formfield_overrides = {
    
    }


class CommentAdmin(admin.ModelAdmin):
    list_display = ["comm_name"]
    formfield_overrides = {
    }

    
class ReplyAdmin(admin.ModelAdmin):
    list_display = ["reply_body"]
    formfield_overrides = {
    }


admin.site.register(Grade, GradeAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(WorkingDays)
admin.site.register(TimeSlots)
admin.site.register(SlotSubject)

