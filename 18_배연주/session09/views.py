from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def choco(request):
    chocos = Choco.objects.all()
    return render(request, 'choco.html', {'chocos': chocos})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})

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
        update_blog = Blog.objects.get(id=id)
        update_blog.title = request.POST['title']
        update_blog.author = request.POST['author']
        update_blog.body = request.POST['body']
        update_blog.save()
        return redirect('detail', update_blog.id)
    else:
        blog = Blog.objects.get(id=id)
        return render(request, 'edit.html', {'blog': blog})

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')

''' Comment '''
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
        update_comment = Comment.objects.get(pk=comment_id)
        update_comment.blog = get_object_or_404(Blog, pk=blog_id)
        update_comment.author = request.POST['author']
        update_comment.content = request.POST['content']
        update_comment.save()
        return redirect('detail', blog_id)
    else:
        blog = Blog.objects.get(pk=blog_id)
        comment = Comment.objects.get(pk=comment_id)
        return render(request, 'edit_comment.html', {'blog': blog, 'comment': comment})

def delete_comment(request, blog_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    # 나중에 user 모델을 만들면 request.user와 작성자가 같은지 확인하는 코드 필요함
    my_comment.delete()
    return redirect('detail', blog_id)