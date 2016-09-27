from django.db import models

from django.utils.timezone import now
from django.contrib.auth.models import User

from django.db.models.signals import post_save

# Create your models here.
class NewsletterSignup(models.Model):

    email = models.EmailField()
    signup_date = models.DateTimeField('Date Signed Up',auto_now_add=True)

    def __str__(self):
        return self.email

class WorkshopUser(models.Model):
    LEVELS = (
    ('0', 'Baby'),
    ('1', 'Student'),
    ('2', 'Teacher'),
    ('3', 'Doctor'),
    ('4', 'Professor'),
    ('5', 'Mad Scientist'),
    ('6', 'Superhero'),
    ('7', 'Alien'),
    ('8', 'Wizard'),
    ('9', 'A.I.'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVELS,max_length=100,default=0)

    def __unicode__(self):
        return self.user

def create_workshop_user(sender, instance, created, **kwargs):
    if created:
        WorkshopUser.objects.create(user=instance)

post_save.connect(create_workshop_user,sender=User)