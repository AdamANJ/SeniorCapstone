from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.

class textContainer(models.Model):
	title						= models.CharField(max_length=100)
	text						= models.TextField()
	order						= models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Section"
		verbose_name_plural = "Sections"
		ordering = ['order']

class imageContainer(models.Model):
	image 						= models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=100)
	welcome						= models.CharField(max_length=200, default='')

	def __str__(self):
		return self.image.name

	def save(self, *args, **kwargs):
		if not self.pk and imageContainer.objects.count() >= 1:
			raise ValidationError("You can only have 1 header.")
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "Header"
		verbose_name_plural = "Header"

class Speaker(models.Model):
	image					= models.ImageField(upload_to="media/speakers/", height_field=None, width_field=None, max_length=100)
	first_name				= models.CharField(max_length=50,default='', verbose_name="First Name")
	last_name				= models.CharField(max_length=50,default='')
	specialty				= models.CharField(max_length=50,default='', verbose_name="Title")
	bio						= models.TextField(default='')
	order					= models.PositiveIntegerField(default=0)

	def __str__(self):
		return (self.first_name + " " + self.last_name)

	class Meta:
		verbose_name = "Speakers"
		verbose_name_plural = "Speakers"
		ordering = ['order']

class Highlighted_Speaker(models.Model):
	image					= models.ImageField(upload_to="media/highlighted_speakers/", height_field=None, width_field=None, max_length=100)
	first_name				= models.CharField(max_length=50,default='', verbose_name="First Name")
	last_name				= models.CharField(max_length=50,default='')
	specialty				= models.CharField(max_length=50,default='', verbose_name="Title")
	bio						= models.TextField(default='')
	order					= models.PositiveIntegerField(default=0)

	def __str__(self):
		return (self.first_name + " " + self.last_name)

	def save(self, *args, **kwargs):
		if not self.pk and Highlighted_Speaker.objects.count() >= 5:
			raise ValidationError("You can only have 5 highlighted speakers.")
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "Highlighted Speaker"
		verbose_name_plural = "Highlighted Speakers"
		ordering = ['order']

class registration(models.Model):
	first_name			= models.CharField(max_length=50)
	last_name			= models.CharField(max_length=50)
	phone				= models.CharField(max_length=15,validators=[MinLengthValidator(9)])
	email				= models.EmailField(max_length=100)
	parent_email		= models.EmailField(max_length=100, verbose_name="Parent's Email", blank=True, null=True)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = "Applicants"
		verbose_name_plural = "Applicants"

class events(models.Model):
	time				= models.CharField(max_length=50)
	name				= models.CharField(max_length=50)
	info				= models.TextField()
	order				= models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Events"
		verbose_name_plural = "Events"
		ordering = ['order']