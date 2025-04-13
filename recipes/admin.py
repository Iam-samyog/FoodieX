from django.contrib import admin
from .models import Recipe, Category
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'cooking_time', 'difficulty', 'created_date')
    list_filter = ('category', 'difficulty', 'author')
    search_fields = ('title', 'description', 'ingredients')
    date_hierarchy = 'created_date'

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
