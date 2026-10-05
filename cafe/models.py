from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.CharField(max_length=50)
    image=models.ImageField(upload_to='menu_images/',blank=True,null=True)

    def __str__(self):
        return self.name