from django.db import models

from django.utils.timezone import now


# Create your models here.
class NewsletterSignup(models.Model):

    email = models.EmailField()
    signup_date = models.DateTimeField('Date Signed Up',auto_now_add=True)

    def __str__(self):
        return self.email