from django.contrib import admin

from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['article_name']}),
        (None,              {'fields': ['article_text']}),
        ('Date information',{'fields': ['pub_date']}),
        (None,              {'fields': ['image']}),
    ]

admin.site.register(Article, ArticleAdmin)
