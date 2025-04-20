from django.db import models

# Create your models here.
class PageVisit(models.Model):
    """
    db -> table
    id -> hidden -> primary key -> auto increment
    """

    # Fields
    
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Visit to {self.path} at {self.timestamp}"