from django.shortcuts import render ,get_object_or_404
from.models import Post,Comment
# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	context ={
		'posts':posts,
	}
	return render(request,'board/blog-grid-3col.html',context)

def post_detail(request,post_pk):
	post = get_object_or_404(Post,pk=post_pk)
	comments = Comment.objects.filter(post_id=post_pk)
	context = {
		"post":post,
		"comments":comments,
	}
	return render(request,'board/blog-single-image-post.html',context)