from django.db import models
from mdeditor.fields import MDTextField #markdown追加
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone
from django.utils.safestring import mark_safe # markdown追加

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) # タイトル(200文字まで)
    # text = MDTextField() #markdown追加
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')#markdown追加
    created = models.DateTimeField(auto_now_add=True,help_text='作成日')
    modified = models.DateTimeField(auto_now=True,help_text='更新日')
    image = models.ImageField(upload_to='media/',blank=True)
    url = models.SlugField(unique=True,primary_key=True) # URL作成

    """ def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Blog, self).save(*args, **kwargs) """

    # markdownを適用できるように設定
    def get_text_markdown(self):
        return mark_safe(markdownify(self.text))

    # このオブジェクトで文字列表現を定義
    def __str__(self):
        return self.title