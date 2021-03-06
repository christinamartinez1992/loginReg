from __future__ import unicode_literals

from django.db import models
import re 


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
	# BASIC VALIDATIONS
	# email must be of format
	# name must have length of at least 4
	# password and password_conf need to match
class UserManager(models.Manager): 
	def validate_reg(self, post_data): 
		# a_user = {}
		errors= {}
		if len(post_data['name']) < 4:
			errors['name'] = "First name should be more than 4 letters"
		if not re.match(EMAIL_REGEX, post_data['email']):
			errors['email'] = "Email must be of correct format."
		if len(post_data['password']) < 8:
			errors['name'] = "Password must be at least 8 characters long"
		if post_data['password'] != post_data['password_conf']:
			errors['password'] = "Password must match password confirmation"
		print errors
		return errors
		
# Create your models here.
class User(models.Model): 
	name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length=255)
	objects = UserManager()

