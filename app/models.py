from __future__ import unicode_literals
from django.db import models as m
from django.contrib.auth.models import User


class Post(m.Model):
	title = m.CharField(max_length=200)
	slug = m.SlugField(unique=True)
	author = m.ForeignKey(User)
	category = m.ForeignKey('Category')
	tag = m.ManyToManyField('Tag')
	b_image = m.ImageField(upload_to='post_background', null=True, blank=True, verbose_name='Header Image')
	sub_header = m.CharField(max_length=200, null=True, blank=True)
	content = m.TextField(null=True, blank=True)
	status = m.BooleanField(default=True)
	created_at = m.DateTimeField(auto_now_add=True)
	updated_at = m.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s' % self.title


class Category(m.Model):
	name = m.CharField(max_length=100)
	slug = m.SlugField(unique=True)
	status = m.BooleanField(default=True)

	def __unicode__(self):
		return '%s' % self.name

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class Tag(m.Model):
	name = m.CharField(max_length=100)
	slug = m.SlugField(unique=True)
	status = m.BooleanField(default=True)

	def __unicode__(self):
		return '%s' % self.name
