from django.shortcuts import render
from app.models import Post, Category, Tag


def index(request):
	posts = Post.objects.filter(status=True)
	data = {'posts': posts}

	return render(request, 'index.html', data)

def detail(request, slug):
	post = Post.objects.get(status=True, slug=slug)
	data = {'post': post}

	return render(request, 'article.html', data)

def category(request, slug):
	category = Category.objects.get(slug=slug)
	posts = Post.objects.filter(status=True, category=category)
	data = {'posts': posts}

	return render(request, 'inner.html', data)

def tag(request, slug):
	tag = Tag.objects.get(slug=slug)
	posts = Post.objects.filter(status=True, tag=tag)
	data = {'posts': posts}

	return render(request, 'inner.html', data)