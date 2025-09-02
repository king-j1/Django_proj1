from django.db import models

# Create your models here.
class Client(models.Model):
      full_name = models.CharField(max_length=100)
      email = models.EmailField(unique=True)
      phone = models.CharField(max_length=15, unique=True)
      address = models.TextField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      city = models.CharField(max_length=50)
      state = models.CharField(max_length=50)
      country = models.CharField(max_length=50)
      zip_code = models.CharField(max_length=10)

      def __str__(self):
        return(f"{self.full_name} - {self.email} - {self.created_at}")
