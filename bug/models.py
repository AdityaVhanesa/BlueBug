from django.db import models

from user.models import Users


# Create your models here.

# Bug Model

class Bugs(models.Model):
    uuid = models.BigIntegerField(unique=True)
    title = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=50, default='open')
    closed_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='closed_by', null=True)
    raised_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='raised_by')
    closed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['uuid']
        db_table = 'bugs'
        get_latest_by = 'uuid'

    def save(self, *args, **kwargs):
        latestBugObject = Bugs.objects.all()
        if not latestBugObject:
            latestBugId = 1
        else:
            latestBugId = int(Bugs.objects.latest().uuid) + 1
        self.uuid = latestBugId
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.uuid)


class Posts(models.Model):
    description = models.TextField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    bug_id = models.ForeignKey(Bugs, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        db_table = 'posts'
        get_latest_by = '-updated_at'

    def __str__(self):
        return f"Linked to Bug {self.bug_id}"
