from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
					super().save()             # Running save method of Parent Class
					
					img = Image.open(self.image.path)
			
					if img.height > 100 and img.width > 100:
						output_size = (100, 100)
						img.thumbnail(output_size)
						img.save(self.image.path)
			
					elif img.height > 100 and img.width < 100:
						output_size = (100, img.width)
						img.thumbnail(output_size)
						img.save(self.image.path)
			
					elif img.height < 100 and img.width > 100:
						output_size = (img.height, 100)
						img.thumbnail(output_size)
						img.save(self.image.path) 