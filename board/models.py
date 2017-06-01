from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	created = models.DateTimeField(default=timezone.now())
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
