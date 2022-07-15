from django.db import models

# Create your models here.
class User(models.Model):
    score=models.CharField(max_length=100,null=True, blank= True)
    fname=models.CharField(max_length=100,null=True, blank= True)
    lname=models.CharField(max_length=100,null=True, blank= True)
    v1=models.CharField(max_length=100,null=True, blank= True)
    v2=models.CharField(max_length=100,null=True, blank= True)
    v3=models.CharField(max_length=100,null=True, blank= True)
    v4=models.CharField(max_length=100,null=True, blank= True)
    v5=models.CharField(max_length=100,null=True, blank= True)
    v6=models.CharField(max_length=100,null=True, blank= True)
    v7=models.CharField(max_length=100,null=True, blank= True)
    v8=models.CharField(max_length=100,null=True, blank= True)
    v9=models.CharField(max_length=100,null=True, blank= True)
    v10=models.CharField(max_length=100,null=True, blank= True)
    v11=models.CharField(max_length=100,null=True, blank= True)
    v12=models.CharField(max_length=100,null=True, blank= True)
    g1=models.CharField(max_length=100,null=True, blank= True)
    g2=models.CharField(max_length=100,null=True, blank= True)
    g3=models.CharField(max_length=100,null=True, blank= True)
    g4=models.CharField(max_length=100,null=True, blank= True)
    g5=models.CharField(max_length=100,null=True, blank= True)
    g6=models.CharField(max_length=100,null=True, blank= True)
    g7=models.CharField(max_length=100,null=True, blank= True)
    g8=models.CharField(max_length=100,null=True, blank= True)
    g9=models.CharField(max_length=100,null=True, blank= True)
    g10=models.CharField(max_length=100,null=True, blank= True)
    l1=models.CharField(max_length=100,null=True, blank= True)
    l2=models.CharField(max_length=100,null=True, blank= True)
    l3=models.CharField(max_length=100,null=True, blank= True)
    l4=models.CharField(max_length=100,null=True, blank= True)
    l5=models.CharField(max_length=100,null=True, blank= True)
    l6=models.CharField(max_length=100,null=True, blank= True)
    l7=models.CharField(max_length=100,null=True, blank= True)
    l8=models.CharField(max_length=100,null=True, blank= True)
    l9=models.CharField(max_length=100,null=True, blank= True)


# class MyModel(models.Model):
#     name = models.CharField(max_length = 100)
#     def __str__(self):
#         return self.name
