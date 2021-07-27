from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.
def home(request):
    cats = Cat.objects.all()
    return render (request, 'home.html', {'cats':cats})

def detail(request, id):
    cat = get_object_or_404(Cat, pk = id)
    return render(request, "detail.html", {"cat":cat})


def make_post(request):
    if request.method == 'POST':
        new_cat = Cat()
        new_cat.title = request.POST['title']
        new_cat.author = request.POST['author']
        new_cat.image = request.FILES.get['image']
        new_cat.body = request.POST['body']
        new_cat.pub_date = timezone.now()
        new_cat.save()
        return redirect('home')
    else:
        return render(request, 'new.html')  

# def edit(request, id):
#     cat = Cat.objects.get(id=id)
#     return render(request, 'edit.html', {'cat':cat})

def update(request, id):
    if request.method == 'POST':
        update_cat = Cat.objects.get(id=id)
        update_cat.title = request.POST['title']
        update_cat.author = request.POST['author']
        update_cat.body = request.POST['body']
        update_cat.save()
        return redirect('detail', update_cat.id)
    else:
        cat = Cat.objects.get(id=id)
        return render(request, 'edit.html', {'cat':cat})


def delete(request, id):
    delete_cat = Cat.objects.get(id=id)
    delete_cat.delete()
    return redirect('home')

def create_comment(request, cat_id):
    if request.method == "POST":
        comment=Comment()
        comment.cat = get_object_or_404(Cat, pk = cat_id)
        comment.author = request.POST['author']
        comment.content = request.POST['content']
        comment.created_at = timezone.datetime.now()
        comment.save()
        return redirect('detail', cat_id)

def delete_comment(request, cat_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    my_comment.delete()
    return redirect('detail', cat_id)

def update_comment(request, cat_id, comment_id):
    if request.method == 'POST':
        up_comment = get_object_or_404(Comment, pk=comment_id)
        up_comment.author = request.POST['author']
        up_comment.content = request.POST['content']
        up_comment.save()
        return redirect('detail', cat_id)
    else:
        cat = get_object_or_404(Cat, pk=cat_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        return render(request, 'comment_edit.html', {'cat':cat, 'comment':comment})    




