from django.db import models

# Create your models here.
    

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.publisher_name, self.address, self.city, self.state}'

class Superhero(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    superhero_name = models.CharField(max_length=20)
    has_comics = models.BooleanField()
    has_toys = models.BooleanField()

    def __str__(self):
        return f'{self.publisher, self.superhero_name, self.has_comics, self.has_toys}'


class Comics(models.Model):  
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    series = models.CharField(max_length=30) 
    issue = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    image = models.CharField(max_length=50,default='s3_image_link')

    def __str__(self):
        return f'{self.publisher, self.superhero, self.series, self.issue, self.price, self.image}'
       


class Toys(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    super_hero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    toy_type = models.CharField(max_length=20)
    toy_name = models.CharField(max_length=20)
    ages = models.CharField(max_length=20)
    image = models.CharField(max_length=50,default='s3_image_link')

    def __str__(self):
        return f'{self.publisher, self.super_hero, self.toy_type, self.toy_name, self.ages, self.image}'






