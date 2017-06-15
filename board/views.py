from django.shortcuts import render ,get_object_or_404
from.models import Post,Comment
from django.contrib.auth import get_user
# Create your views here.
def homepage(request):
	return render(request,'board/homepage.html')


def post_list(request):
	posts = Post.objects.all()
	context ={
		'posts':posts,
	}
	return render(request,'board/blog-grid-3col.html',context)

def post_detail(request,post_pk):

	if request.method =="GET":
		pass
	if request.method =="POST":
		content = request.POST.get('content')
		user = get_user(request)
		comment = Comment.create(content,post_pk,user)
		comment.save()

	post = get_object_or_404(Post,pk=post_pk)
	comments = Comment.objects.filter(post_id=post_pk)
	context = {
		"post":post,
		"comments":comments,
	}
	return render(request,'board/blog-single-image-post.html',context)