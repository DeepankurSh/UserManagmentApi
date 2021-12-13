from django.db import models
from django.core.validators import MaxValueValidator

class users(models.Model):
    first_name = models.CharField(unique =True,max_length= 20)
    last_name = models.CharField(max_length= 20)

    contact_no = models.BigIntegerField(unique = True , validators=[MaxValueValidator(9999999999)])

    def __str__(self):
        return self.first_name


