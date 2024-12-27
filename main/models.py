from django.db import models

# Create your models here.
from .signup.models import User
from django.core.exceptions import ObjectDoesNotExist
from .fitness.models import FitnessBlogPost,WorkoutCategories, FitnessExercise, FitnessEquipment
from django.utils import timezone
from .nutrition.models import Recipe, Guide, Article, Essentials

class MembershipRequest(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Creates a ForeignKey relationship with the User model
    email = models.EmailField(unique=True)
    plan = models.CharField(max_length=100)
    subscription_type = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.plan} ({self.subscription_type})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name}'s Profile"

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=50)
    subscription_type = models.CharField(max_length=10, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')])
    start_date = models.DateField()
    expiry_date = models.DateField()
    email = models.EmailField(unique=True)  # `email` should be unique, but not primary key

    def __str__(self):
        return f"{self.user.first_name}'s Subscription"

class CancellationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    request_date = models.DateTimeField(default=timezone.now)
    cancelled_status = models.BooleanField(default=False)  # False = Pending, True = Processed

    def __str__(self):
        return f"Cancellation Request for {self.user.email} - Status: {'Processed' if self.cancelled_status else 'Pending'}"
    
    
__all__ = ['User', 'FitnessBlogPost', 'WorkoutCategories', 'FitnessExercise', 'FitnessEquipment', 'Recipe', 'Guide', 'Article','Essentials','MembershipRequest', 'CancellationRequest']
