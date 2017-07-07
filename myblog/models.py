from __future__ import unicode_literals

from django.db import models



from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible


class Post(models.Model):

	author = models.CharField(max_length =250)
	title = models.CharField(max_length =250)
	image = models.FileField()
	text = models.TextField()




	def __str__(self):
		return self.title

  