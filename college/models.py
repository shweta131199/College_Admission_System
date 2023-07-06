from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'only alphanumeric characters are allowed.')

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class Application(models.Model):
    COURSES = (
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200, blank=True, null=True, validators=[alphanumeric]) 
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=10) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
    ssc_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    ssc_marksheet = models.ImageField(upload_to="images", null=True)
   
    hsc_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    hsc_marksheet = models.ImageField(upload_to="images", null=True)
   
    cet_percentile = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    cet_scorecard = models.ImageField(upload_to="images", null=True)
    jee_percentile = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    jee_scorecard = models.ImageField(upload_to="images", null=True)
    transfer_certificate = models.ImageField(upload_to="images", null=True)
    income_certificate = models.ImageField(upload_to="images", null=True)
    domacile_certificate = models.ImageField(upload_to="images", null=True)
    cast_certificate = models.ImageField(upload_to="images", null=True)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users')

class Notice(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Detail(models.Model):
    title = models.ForeignKey(Notice, on_delete=models.CASCADE)
    notice = models.CharField(max_length=200)

    def __str__(self):
        return self.notice

class Hostel_Application(models.Model):
    COURSES = (
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200, blank=True, null=True, validators=[alphanumeric]) 
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=10) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
   
    admission_receipt = models.ImageField(upload_to="images", null=True)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Approved")
    message = models.TextField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users')
