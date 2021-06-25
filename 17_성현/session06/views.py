from django.conf.urls import url
from django.shortcuts import render

textThing=''
# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    set(text)
    total_len = len(text)
    unblankText = len(text.replace(" ", ""))
    wordList = text.split(' ')
    countWords = len(wordList)
    return render(request, 'result.html', {'total_len':total_len, 'text':text,'unblankText':unblankText,'wordList':wordList, 'countWords':countWords})

def test(request):
    return render(request, 'test.html') 

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')
