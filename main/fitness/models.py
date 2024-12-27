
from django.db import models
# from signup.models import User

class FitnessBlogPost(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    content = models.TextField()  # Full blog content
    excerpt = models.TextField(max_length=300, blank=True, help_text="A short summary of the post")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets the date when created

    def __str__(self):
        return self.title
    
    
class WorkoutCategories(models.Model):
    title = models.CharField(max_length=200)  # Name of the workout category (e.g., "Strength-Building Workouts")
    overview = models.TextField()  # Overview description of the category

    def __str__(self):
        return self.title

class FitnessExercise(models.Model):
    category = models.ForeignKey(WorkoutCategories, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # Exercise name (e.g., "Compound Lifts")
    description = models.TextField()  # Details about the exercise
    routine = models.TextField(blank=True, null=True)  # Optional field for sample routines
    image = models.ImageField(upload_to='workout_images/', blank=True, null=True)  # Image for the exercise

    def __str__(self):
        return f"{self.name} ({self.category.title})"

class FitnessEquipment(models.Model):
    name = models.CharField(max_length=100)  # Name of the equipment
    description = models.TextField()  # Description of the equipment
    image = models.ImageField(upload_to='equipment_images/')  # Image path
    amazon_link = models.URLField()  # Amazon link for purchasing

    def __str__(self):
        return self.name
