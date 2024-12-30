from django.db import models

# Create your models here.

class pet(models.Model):
    pid=models.AutoField(primary_key=True)
    gender=(("Male","male"),("Female","female"))
    name=models.CharField(max_length=200)
    species=models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(max_length=200,choices=gender)
    description=models.CharField(max_length=500)
    price=models.FloatField()
    is_activate=models.BooleanField(default=False)
    pet_image=models.ImageField(null=True,blank=True,upload_to='images/')

    class Meta:
        db_table="pet"


class customer(models.Model):
    emailId=models.CharField(max_length=200,primary_key=True)
    custname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact_No=models.BigIntegerField()


    class Meta:
        db_table="customer"


class cart(models.Model):
    pet_obj=models.ForeignKey(pet,on_delete=models.CASCADE)
    cust_obj=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    totalprice=models.FloatField(default=0.0)

    class Meta:
        db_table='cart'




class orders(models.Model):
    emailId=models.CharField(max_length=100)
    ordernumber=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phoneno=models.BigIntegerField()
    totalbillamount=models.FloatField(default=0.0)

class adminmodel(models.Model):
    adminemailid=models.CharField(max_length=100, primary_key=True)
    adminpassword=models.CharField(max_length=100)

