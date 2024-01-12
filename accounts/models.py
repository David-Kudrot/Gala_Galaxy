from django.db import models

# Create your models here.
class UserProfileModel(models.Model):
    name=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to="accounts/images")
    shipping_address=models.TextField()
    
    def __str__(self):
        return self.name