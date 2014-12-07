#imports the date
from datetime import date

#imports a bunch of models and helpful stuff (data validators?) from django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models

# localflavor is a sick name. Also imports the django stuff for the US phone number field. Get it? Local flavor.. 
from localflavor.us.models import PhoneNumberField

#defines model class for breaking news alerts with headline, url, and bool for if an alert was sent
class News(models.Model):
	headline = models.CharField(max_length=255)
	url = models.URLField()
	alert_sent = models.BooleanField(default=False)
	
	# because "newss" sounds dumb (django defult pluralization just adds an s)
	class Meta:
		verbose_name_plural = 'news'
		
	# Makes it so that headlines are what show in the admin list for breaking news 
	# (Cuz ain't nobody got time for urls)
	def __unicode__(self):
		return "{}".format(self.headline)

# makes subsciber model with dat demographic info
class Subscriber(models.Model):
	EMPLOYEE = 'E'
	FACULTY = 'F'
	PARENT = 'P'
	ALUM = 'A'
	STUDENT = 'S'
	
	AFFILIATION_CHOICES = (
		(EMPLOYEE, 'Employee'),
		(FACULTY, 'Faculty'),
		(PARENT, 'Parent'),
		(ALUM, 'Alum'),
		(STUDENT, 'Student'),
	)

	MIN_CLASS_YEAR = 1900
	MAX_CLASS_YEAR = date.today().year + 5

	# field definitions 
	user = models.OneToOneField(User)
	affiliation = models.CharField(max_length=1, choices=AFFILIATION_CHOICES)
	class_year = models.PositiveIntegerField(validators=[
		MinValueValidator(MIN_CLASS_YEAR), MaxValueValidator(MAX_CLASS_YEAR)])
	cell_phone = PhoneNumberField()
	
	# makes it so first last username show in database list in admin :) yayyy
	def __unicode__(self):
		return "{} {} ({})".format(self.user.first_name, self.user.last_name, self.user.username)
