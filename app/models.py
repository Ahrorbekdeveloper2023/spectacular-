from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Klass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Praduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    davomiyligi = models.CharField(max_length=100)
    viza = models.CharField(max_length=100)
    decription = models.TextField()
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='product')

    def __str__(self) -> str:
        return self.name