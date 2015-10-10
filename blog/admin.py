from django.contrib import admin
from .models import Categoria, Post



class Postadmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['created_date','published_date',]}),
        ('Content Post',     {'fields': ['categoria', 'titulo','texto']}),
    ]

    list_display = ('titulo', 'created_date', 'was_published')
    search_fields = ['texto']


admin.site.register(Post, Postadmin)
admin.site.register(Categoria)
