from django.contrib import admin
from .models import Article,Comment
# class CommentInine(admin.StackedInline):
#     model=Comment
# class ArticleAdmin(admin.ModelAdmin):
#     inlines=[
#         CommentInine,
#     ]
class CommentInine(admin.TabularInline):
    model=Comment
class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentInine,
    ]
    # StackedInline show in two line
    #TabularInline show in one line
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
