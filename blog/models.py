from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Título")
    summary = RichTextField(null=True, verbose_name="Descição")
    content = RichTextUploadingField(null=True, verbose_name="Conteúdo")
    text = models.CharField(max_length=50, verbose_name="Hashtags")#, widget=models.TextField(attrs={'placeholder': 'Search'}))
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    """class Meta:
        fields_order = ["title", "content", "summary", "text"]"""

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title