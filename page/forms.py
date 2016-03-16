from django import forms as f


class ContactForm(f.Form):
	name = f.CharField(required=True)
	email = f.EmailField(required=True)
	content = f.CharField(required=True)