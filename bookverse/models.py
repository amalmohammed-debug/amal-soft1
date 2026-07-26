from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان الكتاب')
    author = models.CharField(max_length=100, verbose_name='المؤلف')
    description = models.TextField(blank=True, verbose_name='الوصف')
    genre = models.CharField(max_length=50, verbose_name='التصنيف')
    published_year = models.IntegerField(blank=True, null=True, verbose_name='سنة النشر')
    pages = models.IntegerField(blank=True, null=True, verbose_name='عدد الصفحات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')

    class Meta:
        verbose_name = 'كتاب'
        verbose_name_plural = 'الكتب'
        ordering = ['-created_at']

    def __str__(self):
        return self.title