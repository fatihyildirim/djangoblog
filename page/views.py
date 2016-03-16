from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from page.models import Page
from page.forms import ContactForm


def page(request, slug):
	page = get_object_or_404(Page, status=True, slug=slug)

	data = {'page': page}

	if page.slug == 'contact':
		data['form'] = ContactForm

	return render(request, 'inner.html', data)

def contactform(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			# get here code
			return HttpResponseRedirect('/')


	return HttpResponseRedirect('/contact')
		