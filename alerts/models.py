from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models

from localflavor.us.models import PhoneNumberField

class News(models.Model):
	headline = models.CharField(max_length=255)
	url = models.URLField()
	alert_sent = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = 'news'

	def __unicode__(self):
		return "{}".format(self.headline)

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

	user = models.OneToOneField(User)
	affiliation = models.CharField(max_length=1, choices=AFFILIATION_CHOICES)
	class_year = models.PositiveIntegerField(validators=[
		MinValueValidator(MIN_CLASS_YEAR), MaxValueValidator(MAX_CLASS_YEAR)])
	cell_phone = PhoneNumberField()

	def __unicode__(self):
		return "{} {} ({})".format(self.user.first_name, self.user.last_name, self.user.username)
