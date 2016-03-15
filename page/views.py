from django.shortcuts import render, get_object_or_404
from page.models import Page


def page(request, slug):
	page = get_object_or_404(Page, status=True, slug=slug)
	data = {'page': page}

	return render(request, 'inner.html', data)