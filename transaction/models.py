from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    mojoodi = models.PositiveBigIntegerField()
    
    
class Transaction(models.Model):
    from_user = models.OneToOneRel(to=User, on_delete=models.CASCADE)
    to_user = models.OneToOneRel(to=User, on_delete=models.CASCADE)
    money = models.PositiveBigIntegerField()