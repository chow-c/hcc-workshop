from __future__ import unicode_literals

from django.db import models

EDUCATION_CHOICES = (
    ('highschool', 'High School'),
    ('tafe', 'Diploma \ Grad. cert.'),
    ('undergrad', 'Undergradute Degree'),
    ('master', 'Masters Degree'),
    ('phd', 'PhD'),
    ('other', 'Other'),
)

GENDER_CHOICES = (
    ('female', 'Female'),
    ('male', 'Male'),
    ('other', 'I would prefer not to say'),
)

VISION_CHOICES = (
    ('normal', 'Yes'),
    ('abnormal', 'No'),
)

# Sequences are hard coded based on Latin square generation of sequences.
# The first part is the ordering of images: H = heirarchy, R = radial and S = Standard
# The second part is the question sequence - This means that participants are shown 12 questions, 6 for each type of image they view
SEQUENCES = (
    ('1','H,R - 1,2,6,3,5,4'),
    ('2','H,R - 2,3,1,4,6,5'),
    ('3','H,R - 3,4,2,5,1,6'),
    ('4','H,R - 4,5,3,6,2,1'),
    ('5','H,R - 5,6,4,1,3,2'),
    ('6','H,R - 6,1,5,2,4,3'),
    ('7','R,S - 1,2,6,3,5,4'),
    ('8','R,S - 2,3,1,4,6,5'),
    ('9','R,S - 3,4,2,5,1,6'),
    ('10','R,S - 4,5,3,6,2,1'),
    ('11','R,S - 5,6,4,1,3,2'),
    ('12','R,S - 6,1,5,2,4,3'),
    ('13','S,H - 1,2,6,3,5,4'),
    ('14','S,H - 2,3,1,4,6,5'),
    ('15','S,H - 3,4,2,5,1,6'),
    ('16','S,H - 4,5,3,6,2,1'),
    ('17','S,H - 5,6,4,1,3,2'),
    ('18','S,H - 6,1,5,2,4,3'),
)


# Pre-experiment questionnaire
class Questionnaire(models.Model):
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    education = models.CharField(choices=EDUCATION_CHOICES, max_length=100)
    major = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    vision = models.CharField(choices=VISION_CHOICES, max_length=100)

# Form for each experiment page
class ExperimentPage(models.Model):
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    pid = models.IntegerField()
    question_number = models.CharField(max_length=100)
    image_ref = models.CharField(max_length=200)
    answer = models.CharField(max_length=100, blank=True)
    gazedata = models.TextField(blank=True)

# table of questions asked to participants with the associated image and answer
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    question_number = models.IntegerField()
    image_ref = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

# Keep track of the sequences that have already been 
class Sequences(models.Model):
    sequence = models.CharField(choices=SEQUENCES, max_length=100, unique=True)
    tally = models.IntegerField(default=0)
