from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)  # Title of the recipe
    description = models.TextField()  # Short description of the recipe
    image = models.ImageField(upload_to='img/recipes/', blank=True, null=True)  # Image for the recipe
    detailed_instructions = models.TextField()
    ingredients = models.TextField()
    yt_link = models.URLField(blank=True, null=True)  # External link for the full recipe

    def __str__(self):
        return self.title

class Guide(models.Model):
    title = models.CharField(max_length=200)  # Title of the guide
    description = models.TextField()  # Short description of the guide
    image = models.ImageField(upload_to='img/guides/', blank=True, null=True)  # Image for the guide
    content = models.TextField()
    yt_link = models.URLField(blank=True, null=True)  # External link for the full guide

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)  # Title of the article
    description = models.TextField()  # Short description of the article
    image = models.ImageField(upload_to='img/', blank=True, null=True)  # Image for the article
    link = models.URLField(blank=True, null=True)  # External link for the full article
    detailed_info =models.TextField() 

    def __str__(self):
        return self.title
    
class Essentials(models.Model):
    title = models.CharField(max_length=200)  # Title of the article
    description = models.TextField()  # Short description of the article
    image = models.ImageField(upload_to='img/', blank=True, null=True)  # Image for the article
    yt_link = models.URLField(blank=True, null=True)  # External link for the full article

    def __str__(self):
        return self.title


