from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

#링크
def home(request):
    return render(request, 'home.html')

def education(request):
    return render(request, 'education.html')

def edu_detail(request):
    return render(request, 'edu_detail.html')

def write(request):
    return render(request, 'write.html')

def community(request):
    return render(request, 'community_1.html')

def community2(request):
    return render(request, 'community_2.html')

def login(request):
    return render(request, 'login.html')

def view(request):
    blogs = Blog.objects.get(id =3)
    return render(request, 'view.html', {'blog':blogs})

def edit(request):
    return render(request, 'write.html')


#퀴즈
def first (request) :
    blogs = Blog.objects.get(id =1)
    return render (request, 'quiz_nonjQ.html', {'blog':blogs})

def answer (request, ids) :
    blogs = Blog.objects.get(id =ids)
    return render (request, 'quiz_nonjQAnswer.html', {'blog':blogs})

def second (request):
    blogs = Blog.objects.get(id =2)
    return render (request, 'quiz_nonjQ.html', {'blog':blogs})

def create_comment(request, blog_id):
    if request.method == 'POST':
        comment = Comment()
        comment.blog = get_object_or_404(Blog, pk=blog_id)
        comment.content = request.POST['content']
        comment.save()
    return render(request, 'quiz_nonjQ.html', {'blog':comment.blog})

def create_comment2(request, blog_id):
    if request.method == 'POST':
        comment = Comment()
        comment.blog = get_object_or_404(Blog, pk=blog_id)
        comment.bodys = request.POST['bodys']
        comment.writer = request.POST['writer']
        comment.save()
    return render(request, 'view.html', {'blog':comment.blog})

def update_comment(request, blog_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    comments = comment_id
    return render(request, 'updateComment.html', {'blog':my_comment, 'my_content':comments})

def update_comment2(request, blog_id, comment_id):
    if request.method == 'POST':
        my_comment = Comment.objects.get(pk=comment_id)
        my_comment.blog = get_object_or_404(Blog, pk=blog_id)
        my_comment.content = request.POST['content']
        my_comment.save()
        blogs = Blog.objects.get(id =blog_id)
    return render(request, 'quiz_nonjQ.html', {'blog':blogs})