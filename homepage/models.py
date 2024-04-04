from django.db import models

# Create your models here.
class About(models.Model):
    Name = models.CharField(max_length=30,null=True)
    Mobile_No = models.IntegerField(max_length=10,null=True)
    Email = models.EmailField(max_length=255,null=True)
    LinkedIN = models.URLField(max_length=300,null=True)
    Github = models.URLField(max_length=300,null=True)

    def __str__(self):
        return self.Name
    
class Core_Values(models.Model):
    Q1 = models.TextField(max_length=300,null=True)
    Q2 = models.TextField(max_length=300,null=True)
    Q3 = models.TextField(max_length=300,null=True)
    Q4 = models.TextField(max_length=300,null=True)