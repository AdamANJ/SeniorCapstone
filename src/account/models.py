from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Gabriel Pichot (Fixed Error):
# https://stackoverflow.com/questions/31370333/custom-django-user-object-has-no-attribute-has-module-perms

# Create your models here.

# I did not end up using this part.
# I created my own account manager.
# The reason this isn't removed is becuase it's intertwinned in some other code. It's doing nothing and is not important in the rest of the project.

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, password=None):
			if not email:
				raise ValueError("Email is Required")
			if not username:
				raise ValueError("Username is Required")
			if not first_name:
				raise ValueError("Fist Name is Required")
			if not last_name:
				raise ValueError("Last Name is Required")

			user =  self.model (
					email=self.normalize_email(email),
					username=username,
					first_name=first_name,
					last_name=last_name,
				)
			user.set_password(password)
			user.save(using=self.db)
			return user

	def create_superuser(self, email, username, first_name, last_name, password):
		user  = self.create_user(
				email=self.normalize_email(email),
				username=username,
				first_name=first_name,
				last_name=last_name,
				password=password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser, PermissionsMixin):
	email						= models.EmailField(verbose_name="Email", max_length=60, unique=True)
	username					= models.CharField(max_length=30, unique=True)
	first_name					= models.CharField(verbose_name="First Name", max_length=50)
	last_name					= models.CharField(verbose_name="Last Name", max_length=50)
	date_joined 				= models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
	last_login					= models.DateTimeField(verbose_name="Last Login", auto_now_add=True)
	is_admin					= models.BooleanField(default=False)
	is_active					= models.BooleanField(default=True)
	is_staff					= models.BooleanField(default=False)
	is_superuser				= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perm(self, app_label):
		return True
