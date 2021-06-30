from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    transspace = text.replace(" ","")
    nospace = len(transspace)
    word_list = text.split(" ")
    
    return render(request, 'result.html', 
    {'total_len':total_len,'nospace':nospace, 'word_list':word_list})

def test(request):
    return render(request, 'test.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')