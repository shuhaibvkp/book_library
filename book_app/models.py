from django.db import models

# Create your models here.

class addbook(models.Model):
    boname= models.CharField(max_length=30)
    auname= models.CharField(max_length=30)
    bopdf= models.FileField(upload_to='book_app/static')
    boimage= models.FileField(upload_to='book_app/static')
    date= models.DateField(auto_now_add=True)
    def __str__(self):
        return self.boname