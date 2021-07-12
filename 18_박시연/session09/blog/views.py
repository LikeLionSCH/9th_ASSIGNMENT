import blog
from blog.models import Blog
from blog.models import Comment
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.

# home 추가
def home (request) :
    # 블로그의 모든 객체를 가져온다.
    blogs = Blog.objects.all()
    # 딕셔너리 형식으로 home.html에 보내주기 (이름 blogs로.)
    return render (request, 'home.html', {'blogs' : blogs})

def side (request) :
    return render (request, 'side.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog' : blog})

def make_post(request):
    if request.method == 'POST':
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.author = request.POST['author']
        new_blog.image = request.FILES.get('image')
        new_blog.body = request.POST['body']
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('home')
    else:   # GET 메소드일 때
        return render(request, 'new.html')

def update(request, id):
    if request.method == 'POST':
        update_blog = Blog.objects.get(id = id)
        update_blog.title = request.POST['title']
        update_blog.author = request.POST['author']
        update_blog.body = request.POST['body']
        update_blog.save()
        return redirect('detail', update_blog.id)
    else:
        blog = Blog.objects.get(id = id)
        return render(request, 'edit.html', {'blog':blog})

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('home')



'''comment'''
def create_comment(request, blog_id):
    if request.method == 'POST':
        comment = Comment()
        comment.blog = get_object_or_404(Blog, pk=blog_id)
        comment.author = request.POST['author']
        comment.content = request.POST['content']
        comment.created_at = timezone.datetime.now()
        comment.save()
        return redirect('detail', blog_id)

def update_comment(request, blog_id, comment_id):
    if request.method == 'POST':
        update_my_comment = Comment.objects.get(pk=comment_id)
        update_my_comment.author = request.POST['author']
        update_my_comment.content = request.POST['content']
        update_my_comment.save()
        return redirect('detail', blog_id)
    else:
        comment = Comment.objects.get(id=comment_id)
        return render(request, 'editComment.html', {'comment':comment})

def delete_comment(request, blog_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    my_comment.delete()
    return redirect('detail', blog_id)