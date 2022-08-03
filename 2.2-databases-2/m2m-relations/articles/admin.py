from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, ArticleScope, Scope
from django.core.exceptions import ValidationError


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data['is_main'] == True:
                count += 1
        if count < 1:    
            raise ValidationError('Укажите основной раздел')
        elif count > 1:    
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ArticleScopeInline, ]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']
