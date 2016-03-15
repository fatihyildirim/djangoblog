from django.shortcuts import render
from app.models import Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	posts = Post.objects.filter(status=True).order_by('-created_at')
	paginator = Paginator(posts, 5)

	page = request.GET.get('page')

	try:
		post_per_page = paginator.page(page)
	except PageNotAnInteger:
		post_per_page = paginator.page(1)
	except EmptyPage:
		post_per_page = paginator.page(paginator.num_pages)

	data = {'posts': posts}
	data['post_per_page'] = post_per_page

	return render(request, 'index.html', data)

def detail(request, slug):
	post = Post.objects.get(status=True, slug=slug)
	data = {'post': post}

	return render(request, 'post.html', data)

def category(request, slug):
	category = Category.objects.get(slug=slug)
	posts = Post.objects.filter(status=True, category=category)
	data = {'posts': posts}
	data['page'] = category 

	return render(request, 'result.html', data)

def tag(request, slug):
	tag = Tag.objects.get(slug=slug)
	posts = Post.objects.filter(status=True, tag=tag)
	data = {'posts': posts}
	data['page'] = tag

	return render(request, 'result.html', data)