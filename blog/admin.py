from django.contrib import admin
from blog.models import Article,Author,Category
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article)
