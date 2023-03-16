from django.db import models

# Create your models here.

class Task(models.Model):
    
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    duration=models.DurationField()
    description=models.TextField(null=True, blank=True)

    class Meta:
        ordering=['-updated', '-created']

    def __str__(self):
        return self.name
