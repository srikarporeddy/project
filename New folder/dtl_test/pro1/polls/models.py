from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
class Choice(models.Model):
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	
'''	"""docstring for Choice"models.Modelf 
	choice_text=models.Charfield(max_legth=200)
	votes=models.IntegerField(default=0)
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	__init__(self, arg):
		super(Choice,models.Model._
		choice_text=models.Charfield(max_legth=200)
		votes=models.IntegerField(default=0)
		question=models.ForeignKey(Question,on_delete=models.CASCADE)
		init__()
		self.arg = arg
		
	"""docstring for  Question(models.Modelf 
	question_text=models.charfield(max_length=200)
	pub_date=models.DateTimeField('date published')__init__(self, arg):
		super( Question(models.Model._
		question_text=models.charfield(max_length=200)
		pub_date=models.DateTimeField('date published')_init__()
		self.arg = arg
		'''