from django.db import models

# Create your models here.

def file_location(instance, filename):
    if instance.other_name:
        return "{} {} {}/WorkEvidence/{}".format(instance.last_name, instance.first_name, instance.other_name, filename)
    else:
        return "{} {}/WorkEvidence/{}".format(instance.last_name, instance.first_name, filename)
        
def image_location(instance, filename):
    if instance.other_name:
        return "{} {} {}/passport/{}".format(instance.last_name, instance.first_name, instance.other_name, filename)
    else:
        return "{} {}/passport/{}".format(instance.last_name, instance.first_name, filename)

class Professional(models.Model):
    # Personal information fields
    last_name= models.CharField(max_length=150)
    first_name= models.CharField(max_length=150)
    other_name= models.CharField(max_length=150, blank=True, null=True)
    email= models.EmailField(max_length=150)
    phone= models.CharField(max_length=15)
    gender= models.CharField(max_length=50)
    date_of_birth= models.DateField()
    education_qualification= models.CharField(max_length=150)

    # Address fields
    street= models.CharField(max_length=150)
    city= models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    # Other information
    shop_location= models.CharField(max_length=150)
    internet_usage= models.CharField(max_length=50)
    skill= models.CharField(max_length=500)
    working_duration= models.CharField(max_length=50)
    deadline_handling= models.TextField(max_length=500)
    project= models.TextField(max_length=500)
    home_service= models.CharField(max_length=50)
    expectation= models.TextField(max_length=500)
    relevant_information=models.TextField(max_length=500)

    # Image upload
    passport= models.ImageField(upload_to=image_location, blank=True)
    work_evidence= models.FileField(upload_to=file_location, blank=True)
    # validation
    approved= models.BooleanField(default=False)

    def __str__(self):
        return self.last_name




# class Client(models.Model):
#     request= models.TextField()
#     work_duration= models.CharField()
#     budget= models.IntegerField()
#     full_name= models.CharField()
#     phone_number=models.IntegerField()
#     email= models.EmailField()
#     about= models.TextField()
