from django.db import models

area_type_role = (
    ("1" , "restaurant"),
    ("2" , "pubs"),
    ("3" , "offices"),

)

class UserRegister(models.Model):
    photo = models.ImageField(default=None)
    username = models.CharField(max_length=100,default=None)
    email= models.EmailField()
    phone_number = models.CharField(max_length=10,null=True)
    home_address = models.TextField(max_length=200,null=True)
    dob = models.DateField()

    def __str__(self):
        return self.username

class OwnerRegister(models.Model):
    area_name = models.CharField(max_length=100,null=True)
    area_address = models.TextField(max_length=200,null=True)
    area_type = models.CharField(choices=area_type_role,max_length=10,null=True)
    area_capacity = models.IntegerField()
    contact_number = models.IntegerField

    def __str__(self):
        return self.area_name

    class Meta:
        ordering = ['-id']

class ControlledAreaStaff(models.Model):
    customer = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    number_of_persons_status = models.BooleanField(default=True)
    availability = models.BooleanField(default=False)


