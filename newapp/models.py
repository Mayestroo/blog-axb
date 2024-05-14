from django.db import models

# Create your models here.
class Mahsulot(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Sotuvchi(models.Model):
    nomi = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    narxi = models.IntegerField()
    soni = models.IntegerField()
    
    def __str__(self):
        return str(self.nomi)