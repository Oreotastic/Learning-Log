from django.db import models

# Create your models here.

# Add topic to learn
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# Add an Entry to a Topic.
class Entry(models.Model):
    """Something specifically learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] +  "..."
        else:
            return self.text
