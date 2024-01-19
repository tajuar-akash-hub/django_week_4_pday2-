from django.db import models
from musicians.models import musician_Model


# Create your models here.
class albums_Model(models.Model):
    album_name = models.CharField( max_length=50)
    Artist = models.ForeignKey(musician_Model, on_delete=models.CASCADE,default="Akash")
    album_release_date= models.DateField()

    

    album_ratings_list = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        
    }
    album_rating = models.CharField(max_length=10,choices =album_ratings_list)

    def __str__(self) -> str:
        return f'{self.album_name}'
