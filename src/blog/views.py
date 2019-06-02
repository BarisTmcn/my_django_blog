from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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

@login_required
def blog_post_create_view(request):
	#create objects using a form
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
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
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = "form.html" 
	context = {"form": form, "title": f"Update {obj.title}"}
	return render(request, template_name, context)

def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = "blog/delete.html"
	context = {"object": obj}
	return