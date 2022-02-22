from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os
from embed_video.fields import EmbedVideoField



class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #Get filename
    if instance.subject_id:
        filename = 'Subject_Picture/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='subjects')
    image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)

def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #Get filename
    if instance.lesson_id:
        fielname = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
    return os.path.join(upload_to, filename)


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    lesson_id = models.CharField(max_length=200, unique=True)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=250)
    position = models.PositiveBigIntegerField(verbose_name="Chapter no.")
    slug = models.SlugField(null=True, blank=True)
    videolink = EmbedVideoField(verbose_name="Video link", blank=True, null=True)  
    video = models.FileField(upload_to=save_lesson_files, verbose_name="Video", blank=True, null=True)
    ppt = models.FileField(upload_to=save_lesson_files, verbose_name="Presentations", blank=True)
    Notes = models.FileField(upload_to=save_lesson_files, verbose_name="Notes", blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('school:lesson_list', kwargs={'slug':self.subject.slug, 'grade':self.Grade.slug})

class WorkingDays(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade_days')
    day = models.CharField(max_length=200)

    def __str__(self):
        return self.day


class TimeSlots(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade_time_slots')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + '-' + str(self.end_time)

class SlotSubject(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade_slots')
    day = models.ForeignKey(WorkingDays, on_delete=models.CASCADE, related_name='grade_slots_days')
    slot = models.ForeignKey(TimeSlots, on_delete=models.CASCADE, related_name='grade_slots_time')
    slot_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grade_slots_subject')

    def __str__(self):
        return str(self.grade)+ ' - ' + str(self.day) + ' - ' + str(self.slot) + ' - ' + str(self.slot_subject)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    lesson_name = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name='comments')
    comm_name = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

    
class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)







