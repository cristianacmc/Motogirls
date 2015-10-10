from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Post(models.Model):
    categoria = models.ForeignKey('Categoria')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    def was_published(self):
        if self.published_date is not None:
            return 'ok'
        else:
            return '-'
            was_published.admin_order_field = 'published_date'
            was_published.short_description = 'Published ?'
