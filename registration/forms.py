from django import forms
from registration.models import Professional
from cloudinary.forms import CloudinaryFileField

class ProfessionalForm(forms.ModelForm):
    # Personal information fields
    last_name= forms.CharField(required=True, label="Last Name")
    first_name= forms.CharField(required=True, label="First Name")
    other_name= forms.CharField(required=False, label="Other Name")
    gender= forms.CharField(required=True, label="Gender")
    date_of_birth= forms.DateField(label="dd/mm/yyy")
    education_qualification= forms.CharField(required=True, label="Highest education qualification")

    # Address fields
    street= forms.CharField(required=True, label="Street, nbr")
    city= forms.CharField(required=True, label="City")
    country = forms.CharField(required=True, label="Country")

    # Other information
    shop_location= forms.CharField(required=True, label="Shop/Office location")
    internet_usage= forms.CharField(required=True, label="Can you make use of internet")
    skill= forms.CharField(required=True, label="What is your speciality, skill and strength")
    working_duration= forms.CharField(required=True, label="How long have you been working with your skill(s)")
    deadline_handling= forms.CharField(required=True, label="Can you describe how you handle tight schedule")
    project= forms.CharField(required=True, label="What is the most interesting project you have embarked on")
    home_service= forms.CharField(required=True, label="Can you do home service")
    expectation= forms.CharField(required=True, label="What do you expect from A'SERVICES")
    relevant_information=forms.CharField(required=True, label="Any other relevant information")

    # Image upload
    work_evidence= CloudinaryFileField(required=True)

    class Meta:
        model= Professional
        fields= '__all__'
