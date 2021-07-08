from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import *
# Create your views here.
def study(request):
    studys = Study.objects.all()
    return render (request, 'study.html', {'studys':studys})

def study_detail(request, id):
    study = get_object_or_404(Study, pk=id)
    return render(request, 'study_detail.html', {'study':study})

def study_post(request):
    if request.method == 'POST':
        study_new = Study()
        study_new.title = request.POST['title']
        study_new.author = request.POST['author']
        study_new.image = request.FILES['image']
        study_new.body = request.POST['body']
        study_new.pub_date = timezone.now()
        study_new.save()
        return redirect('study')
    else:
        return render(request, 'study_new.html')

def study_update(request, id):
    if request.method == 'POST':
        update_study = Study.objects.get(id=id)
        update_study.title = request.POST['title']
        update_study.author = request.POST['author']
        update_study.body = request.POST['body']
        update_study.save()
        return redirect('study_detail', update_study.id)
    else:
        study = Study.objects.get(id=id)
        return render(request, 'study_edit.html', {'study':study})

def study_delete(request, id):
    delete_study = Study.objects.get(id=id)
    delete_study.delete()
    return redirect('study')