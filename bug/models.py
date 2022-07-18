from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Bug Model

class Bugs(models.Model):
    title = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=50, default='open')
    found_in = models.CharField(max_length=50)
    severity_level = models.CharField(max_length=50, default="LEVEL - 3")
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='closed_by', null=True)
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raised_by')
    closed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        db_table = 'bugs'
        get_latest_by = '-updated_at'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class Posts(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bugs, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at']
        db_table = 'posts'
        get_latest_by = 'updated_at'

    def __str__(self):
        return f"Linked to Bug {self.bug_id}"


class CustomUser(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.get_full_name()
