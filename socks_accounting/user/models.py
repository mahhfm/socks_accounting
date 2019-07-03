from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

class Origin(models.Model):
    created_date =models.DateTimeField( auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Profile(Origin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=155)
    telegram_id = models.CharField(max_length=155)
    avatar =  models.ImageField(upload_to='avatar/' , default='/avatar/defaults.png')
    active = models.BooleanField()


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name 
    class Meta:
        pass


class Service(Origin):
    SOCKS, HTTP, PPTP, KERIO, OPENVPN = 'socks', 'http', 'pptp', 'kerio', 'openvpn'
    SERVICE_CHOICES = (
        (SOCKS, "socks"),
        (HTTP, "http"),
        (PPTP, "pptp"),
        (KERIO, "kerio"),
        (OPENVPN, "openvpn"),
    )    
    service_name = models.CharField(max_length=155, choices=SERVICE_CHOICES, verbose_name="نو ع سرویس")
    active = models.BooleanField()


class  Order(Origin):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, db_constraint=False)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, db_constraint=False)
    unit = models.IntegerField()
    active = models.BooleanField()
    present_date = models.DateField(default=timezone.now)



    