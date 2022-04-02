from django.db import models

# Create your models here.
class Guitar(models.Model):

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    #Refactor later to provide ist of years
    year = models.IntegerField()
    #Refactor later to provide decimal
    price = models.IntegerField()
    string_count = models.IntegerField()
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ['brand']
