from django.shortcuts import render
from django.conf.urls import url

def count(request):
    return render(request, 'count.html')

# Create your views here.
def result(request):
    text = request.POST['text']
    total_len = len(text)
    notblank = len(text.replace("", " "))
    list = text.split(" ")
    count = len(list)
    return render(request, 'result.html', {
        'text': text, 'total_len' : total_len, 'notblank': notblank, 'list': list, 'count': count
        })

def test(request):
    return render(request, 'test.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')