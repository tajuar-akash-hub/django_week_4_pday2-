from django.db import models

# Create your models here.
class musician_Model(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'
