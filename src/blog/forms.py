from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'slug', 'content']

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		print(email)
		if email.endswith(".edu"):
			raise forms.ValidationError("This is not a valid email.Please don't use  .edu")
		return email

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexactS=title)
		if qs.exists():
			raise forms.ValidationError("This title already been used. Please try again.")
		return title	
