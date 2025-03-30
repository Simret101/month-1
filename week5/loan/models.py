from django.db import models

class Loan(models.Model):
    name=models.CharField(max_length=100)
    amount=models.FloatField()
    date=models.DateField()
    reason=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name+''+self.amount+''+self.date+''+self.reason
    