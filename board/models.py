from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	created = models.DateTimeField(default=timezone.now)
	modified = models.DateTimeField(auto_now=True)
	image = models.ImageField(blank=True, upload_to="media/post/%Y%m")

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	created = models.DateTimeField(default=timezone.now)
	content = models.CharField(max_length=300)

	def __str__(self):
		return str(self.author) + self.content[0:10] +"......"
	 
	@classmethod
	def create(cls,content,post_pk,user):
		comment =cls(content=content, author =user,post_id=post_pk)
		return comment