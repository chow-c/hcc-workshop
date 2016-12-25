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

class CompletedActivity(models.Model):
    completed_date = models.DateTimeField('Date Completed',auto_now_add=True)
    activity = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'completed activity'
        verbose_name_plural = 'completed activity'
        ordering = ('activity',)

class WorkshopUser(models.Model):
    LEVELS = (
        ('0', '0 - Baby'),
        ('1', '1 - Student'),
        ('2', '2 - Master'),
        ('3', '3 - Teacher'),
        ('4', '4 - Researcher'),
        ('5', '5 - Doctor'),
        ('6', '6 - Professor'),
        ('7', '7 - Astronaut'),
        ('8', '8 - Mad Scientist'),
        ('9', '9 - Superhero'),
        ('10', '10 - Alien'),
        ('11', '11 - Wizard'),
        ('12', '12 - A.I.'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVELS, max_length=100, default='0')
    ethics_approval = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'workshop details'
        verbose_name_plural = 'workshop details'

def create_workshop_user(sender, instance, created, **kwargs):
    if created:
        WorkshopUser.objects.create(user=instance)

post_save.connect(create_workshop_user,sender=User)