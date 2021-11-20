from django.db import models
from mdeditor.fields import MDTextField #markdown追加
from markdownx.models import MarkdownxField
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) # タイトル(200文字まで)
    # text = MDTextField() #markdown追加
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')#markdown追加
    created = models.DateTimeField(help_text='作成日')
    modified = models.DateTimeField(help_text='更新日')
    image = models.ImageField(upload_to='media/',blank=True)
    #url = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Blog, self).save(*args, **kwargs)
