from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

class users(models.Model):
    contactNumberRegex = RegexValidator( regex= r"^[6-9]\d{9}$")
    email_idRegex = RegexValidator(regex=r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")
    first_name = models.CharField(unique =True,max_length= 20)
    last_name = models.CharField(max_length= 20)
    contact_no = models.CharField( validators=[contactNumberRegex],max_length=10,unique= True)
    email_Id = models.CharField(validators=[email_idRegex], max_length=320, unique=True,null= True ,blank= True)

    def __str__(self):
        return self.first_name


