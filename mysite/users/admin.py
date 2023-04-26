from django.contrib import admin

from .models import Users, Vehicle, Doctor, BasicData, HealthyData, account

# Register your models here.
admin.site.register(Doctor)
admin.site.register(BasicData)
admin.site.register(HealthyData)
admin.site.register(Users)
admin.site.register(Vehicle)
admin.site.register(account)

