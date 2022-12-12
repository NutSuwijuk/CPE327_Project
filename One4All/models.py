from pydoc import describe
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)

# =========================================================================================================
# class Food(models.Model):
#     name_food = models.CharField(max_length=15,primary_key=True)
#     urls_food = models.CharField(max_length=100)
#     thumb = models.FileField(upload_to = "thumb/%y",blank = True)
#     class Meta:
#         db_table = "food"
#         managed = False
#     def __str__(self):
#         return self.name_food
        
class Person(models.Model):
    no = models.FloatField()
    title = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
# ============================================================================================================


