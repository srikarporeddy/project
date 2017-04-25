from __future__ import unicode_literals

from django.db import models

# Create your models here.
class posts(models.Model):
	author=models.CharField(max_length = 30)
	title=models.CharField(max_length = 100)
	bodytext=models.TextField()
	timestamp=models.DateTimeField()
	"""docstri
ng for posts"models.model) __init__(self, arg):
		super(posts,models.model)__init__()
		self.arg = arg"""