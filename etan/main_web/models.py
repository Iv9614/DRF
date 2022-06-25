from statistics import mode
from django.db import models

# Create your models here.

class taipei (mode.Model):
    area = models.CharField(max_length=20)
    layer = models.CharField(max_length=20)
    build_type = models.CharField(max_length=20)
  

    class Meta:
        db_table = "aig_counter_types"

    def __str__(self):
        return self.area

        
class city (models.Model):

    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=20)

    class Meta:
        db_table = "aig_counter_types"

    def __str__(self):
        return self.text