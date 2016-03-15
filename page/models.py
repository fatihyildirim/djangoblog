from __future__ import unicode_literals
from django.db import models as m


class Page(m.Model):
	title = m.CharField(max_length = 100)
	slug = m.SlugField(unique = True)
	description = m.TextField(blank = True, null = True)
	sub_header = m.CharField(max_length = 100, blank = True, null = True)
	content = m.TextField(blank = True, null = True)
	status = m.BooleanField(default = True)
	created_at = m.DateTimeField(auto_now_add=True)
	updated_at = m.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s' % (self.title)
