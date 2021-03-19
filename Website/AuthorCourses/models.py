from django.db import models

# Create your models here.
from .validators import validate_file


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)

    document = models.FileField(upload_to='documents/', validators=[validate_file])

    def __str__(self):
        return "Name: " + self.description + " || Location: " + str(self.document)


class AllContents(models.Model):
    class Meta:
        verbose_name_plural = 'all contents'

    contentName = models.CharField(max_length=200)
    contentBody = models.CharField(max_length=100)
    contentSummary = models.CharField(max_length=60)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    doc = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return self.contentName
