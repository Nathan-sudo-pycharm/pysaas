from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db->table
    # id-> primary key -> autofield -> 1,2,3,4
    path=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    pass