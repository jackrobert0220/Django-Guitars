from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
ACTIVE_CHOICES = (
    ("Yes", "Yes"),
    ("No", "No"),
)

class Pickup(models.Model):
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    active = models.CharField(max_length=3, choices=ACTIVE_CHOICES)

    def __str__(self):
        return self.type 

YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Guitar(models.Model):

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    #Refactor later to provide ist of years
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    #Refactor later to provide decimal
    price = models.IntegerField()
    string_count = models.IntegerField()
    color = models.CharField(max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to="images/")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickups = models.ManyToManyField(Pickup)
    email = models.EmailField(max_length = 50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ['brand']
