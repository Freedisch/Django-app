from distutils.command.upload import upload
from email.policy import default
from time import timezone
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.db import models
import datetime

# Create your models here.
# Define your first model from here:
class Userorm(models.Model):
    #Charfield for first name
    first_name = models.CharField(null=False, max_length=30, default='Joe')
    #Charfield for last name
    last_name = models.CharField(null=False, max_length=30, default='Chris')
    #Charfield for username
    username = models.CharField(null=True, max_length=30, default='trap45')  
    #Charfield for user's date birth
    dob = models.DateField(null=True)

    # Create a toString 
    def __str__(self):
        return self.first_name + " " + self.last_name

# Creating a One-to-One relationship by heriting from the User model
class Instructor(Userorm):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    #Create a toString method for object string representation
    def __str__(self):
        return "First name:" + self.first_name + "," + \
                " Last name:" + self.last_name + "," + \
                "Is full time:" + str(self.full_time) + ", " + \
                "Total Learners:" + str(self.total_learners)

#Creating the learner model that inherite from the User model
class Learner(Userorm):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
            "Last name: " + self.last_name + ", " + \
            "Date of birth: " + str(self.dob) + ", " + \
            "Occupation: " + self.occupation +", "+ \
            "Social Link: " + self.social_link

# Course model Many to Many relationship
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    image = models.ImageField(upload_to='course_images/', null=True)
    description = models.CharField(max_length=500)
    #Many-to-many relationship with Instructor 
    instructors = models.ManyToManyField(Instructor)
    #Many to Many relationship with learners
    learner = models.ManyToManyField(Learner, through='Enrollement')
    total_enrollment = models.IntegerField(default=0)
    is_enrolled = False
    # Create a toString method for object stribg representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# Enrollment model 
class Enrollement(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # Add a learner foreign key One to Many relationship
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key One to Many relationship
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(null=True)
    #Enrollement mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

# Creating a OnetoMany Relationship 
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()