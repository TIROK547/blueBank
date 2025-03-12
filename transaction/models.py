from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    mojoodi = models.PositiveBigIntegerField()


class Transaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions')
    money = models.PositiveBigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True) 