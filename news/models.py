from django.db import models


class ListCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class News(models.Model):
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='static/images')
    created_at=models.DateTimeField()
    category = models.ForeignKey('ListCategory', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

# Create your models here.
