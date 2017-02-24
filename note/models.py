from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='標籤名稱')

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tag = models.ForeignKey(Tag, verbose_name="標籤", null=True, blank=True)




