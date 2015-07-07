from django.db import models

# Create your models here.

class login_info(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=40)
    usertype= models.CharField(max_length=30,default='user')

class user_info(models.Model):
	username = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

class category(models.Model):
	cat_id=models.BigIntegerField(unique=True,default=0);
	cat_name=models.CharField(max_length=30)
	parent=models.CharField(max_length=30)
	pathp=models.CharField(max_length=500)
	parent_name=models.CharField(max_length=30)

class product(models.Model):
	product_id=models.BigIntegerField(unique=True)
	product_name=models.CharField(max_length=50)
	product_cat=models.CharField(max_length=300)
	product_features=models.CharField(max_length=1000)


class comment(models.Model):
	comment_id=models.BigIntegerField(unique=True)
	username=models.CharField(max_length=30)
	comment_discription=models.CharField(max_length=5000)
	product_id=models.BigIntegerField()
	