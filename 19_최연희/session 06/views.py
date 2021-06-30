from django.shortcuts import render

# Create your views here.
def test1(request):
    return render(request, 'test1.html')

def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')   

def home(request):
    return render(request, 'home.html')

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    blank_len = len(''.join(text.split(" ")))
    list_text = text.split(' ')
    return render(request, 'result.html', {
        'total_len' : total_len, 'blank_len' : blank_len, 'list_text' : list_text 
    })

