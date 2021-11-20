# データベースについて

## djangoの設定
```
$ pip install psycopg2-binary
```
setting.py を変更

新しくDjangoアプリを作成する場合はDBももう一度作った方がいい

# モデルについて
```
$ pip install django-mdeditor
$ pip install django-markdownx ← こっちの方が良いかも 参考(https://blog.narito.ninja/detail/102)
```
# ビューの追加
myapp > views.py 以下を追加<br>
```python
from django.views.generic import DetailView
class BlogDetailView(DetailView):
    model = Blog # 忘れないように
    template_name = "blogs/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "MyPage"
        return context
```

