from django.db import models

# Create your models here.
class Write(models.Model):
    content=models.TextField()
    category_choices = (
        ('Video','Video'),
        ('Design','Design'),
        ('Photo','Photo'),
        ('Web','Web'),
        ('Composing','Composing'),
        ('Product Manager','Product Manager'),
        ('IOS','IOS'),
        ('Lyric','Lyric'),
        ('Vocal','Vocal'),
        ('Android','Android'),
        ('Marketing','Marketing'),
        ('Dance','Dance'),
        ('Server','Server'),
        ('Advertisement','Advertisement'),
        ('etc','etc'),
    )
    category=models.CharField(max_length=20, choices=category_choices,null=True)
    
    def __str__(self):
        return f'{self.content} [{self.id}]'
    