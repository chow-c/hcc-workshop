from django.db import models

from django.utils.timezone import now
from django.contrib.auth.models import User

from django.db.models.signals import post_save

# Create your models here.
class NewsletterSignup(models.Model):

    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    school = models.CharField(max_length=50, null=True, blank=False)
    year = models.CharField(max_length=50, null=True, blank=False)
    area_of_interest = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField()
    signup_date = models.DateTimeField('Date Signed Up', auto_now_add=True)

    def __str__(self):
        return self.email

class CompletedActivity(models.Model):
    completed_date = models.DateTimeField('Date Completed', auto_now_add=True)
    activity = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'completed activity'
        verbose_name_plural = 'completed activity'
        ordering = ('activity',)

class WorkshopUser(models.Model):
    LEVELS = (
        ('0', '0 - Baby'),
        ('1', '1 - Pre-schooler'),
        ('2', '2 - Primary-schooler'),
        ('3', '3 - Teenager'),
        ('4', '4 - Undergraduate'),
        ('5', '5 - Master'),
        ('6', '6 - Teacher'),
        ('7', '7 - Doctor'),
        ('8', '8 - Researcher'),
        ('9', '9 - Professor'),
        ('10', '10 - Astronaut'),
        ('11', '11 - Mad Scientist'),
        ('12', '12 - Superhero'),
        ('13', '13 - Advanced Alien'),
        ('14', '14 - Wizard'),
        ('15', '15 - Supercomputer'),
        ('16', '16 - Skynet'),
        ('17', '17 - Unicorn'),
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

post_save.connect(create_workshop_user, sender=User)
