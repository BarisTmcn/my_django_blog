from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm






#CRUD (create, retrieve, update, delete)

#GET --> retireve/list
#POST --> create/update/delete

def blog_post_list_view(request):
	#list out objects,maybe search
	qs = BlogPost.objects.all()
	template_name = "blog/list.html"
	context = {"object_list": qs}
	return render(request, template_name, context)

def blog_post_create_view(request):
	#create objects using a form
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		form = BlogPostModelForm()
	template_name = "form.html"
	context = {"form": form}
	return render(request, template_name, context)

def blog_post_detail_view(request, slug):
	# 1 object-->detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = "blog/detail.html"
	context = {"object": obj}
	return render(request, template_name, context)

def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = "blog/update.html"
	context = {"object": obj, "form": None}
	return

def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = "blog/delete.html"
	context = {"object": obj}
	return