from django.db import models

# Create your models here.

class Sample(models.Model):
    name = models.CharField(max_length=20)
    mob = models.PositiveBigIntegerField()
    email = models.EmailField(null=True)
    loc = models.CharField(max_length=20)
    
class Indexdb(Sample):
        class Meta:
            proxy=True
    
  