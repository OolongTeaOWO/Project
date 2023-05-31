from django.db import models

# Create your models here.
class Users(models.Model):
	level_list = (('ordinary','Ordinary'),('medical','Medical'))
	name = models.CharField(max_length = 20) # 監控人的名稱
	level = models.CharField(choices=level_list, max_length=20) # 監控人的帳號級別
	phone = models.CharField(max_length = 20) # 監控人的電話號碼

	def __str__(self):
		return self.name

class Account(models.Model):
	e_mail = models.EmailField(max_length = 254) #E-mail
	password = models.CharField(max_length = 15) #密碼

	def __str__(self):
		return self.e_mail

class Vehicle(models.Model):
	name = models.CharField(max_length = 20) #穿戴者名稱

	def __str__(self):
		return self.name

class Doctor(models.Model):
	genders = (('F','Female'),('M','Male'))
	doctor_name = models.CharField(max_length = 20) #醫師名稱
	gender = models.CharField(choices=genders, max_length=20) #醫師性別

	def __str__(self):
		return self.doctor_name

class BasicData(models.Model):
	genders = (('F','Female'),('M','Male'))
	basicData_name =  models.CharField(max_length = 20) #穿戴者名稱
	addres  = models.CharField(max_length = 100) #穿戴者住址
	age  = models.IntegerField(blank= True) #穿戴者年齡
	gender = models.CharField(choices=genders, max_length=20) #穿戴者性別

	def __str__(self):
		return self.basicData_name

class HealthyData(models.Model):
	healthydata_name =  models.DateField(auto_now_add=True) #日期
	blood_oxygen = models.IntegerField(blank= True) #血氧濃度
	heartbeat = models.IntegerField(blank= True) #心跳
	longitude = models.DecimalField(max_digits=12, decimal_places=2) #經度
	latitude = models.DecimalField(max_digits=12, decimal_places=2) #緯度

	def __str__(self):
		return self.healthydata_name
