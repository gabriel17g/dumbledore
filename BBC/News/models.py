from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField(max_length=6000)
    reporter = models.CharField(max_length=200)
    images = models.ImageField(upload_to="News_images", blank=True, null=True)
    date_reported = models.DateTimeField(auto_now_add=None)


    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.headline    
        


# Create your models here.
