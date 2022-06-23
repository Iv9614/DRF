from typing_extensions import Self
from django.db import models

# Create your models here.

# Create your models here.
class build_info(models.Model):

    build_area = models.CharField(max_length=20 ,blank=True ,help_text='鄉鎮市區')
    total_number_floors = models.CharField(max_length=20 , blank=True,help_text='總樓層數') 
    build_type = models.CharField(max_length=20 ,blank=True,help_text= '建物型態')
    build_city = models.CharField(max_length=20, blank=True,help_text= '建物城市')
    #  以下省略 ...

    class Meta:
        db_table = "build_info"
        ordering = ["build_city"]

    def __str__(self):
        return self.build_area
