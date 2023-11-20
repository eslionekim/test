from django.db import models

# Create your models here.
class Write(models.Model):
    content=models.TextField()
    comment=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.content} [{self.id}]'
    