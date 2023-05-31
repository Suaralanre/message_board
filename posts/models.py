from django.db import models

# Create your models here.
class Post(models.Model):
    '''Remember in ORM, the class name represents the table. 
    The attributes are the columns and each object 
    instance represents a row in the table.
    Table => Post
   Column => text
    Row => each instance of Post
    '''
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:50]