from django.db import models

'''
id
title
content
created_at
photo
'''
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')

    def _str_(self):
        return self.title




