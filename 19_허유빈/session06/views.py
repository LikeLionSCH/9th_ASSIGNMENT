from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request,'count.html')

def result(request):
    text = request.POST['text']
    text_count = len(text)
    text_countWithoutSpace = len(text.replace(" ",""))
    word_list = text.split()
    return render(request, 'result.html', {
        'text_count' : text_count, 'text_countWithoutSpace' : text_countWithoutSpace, 'word_list' : word_list
    })

def test(request):
    return render(request,'test.html')

def test1(request):
    return render(request,'test1.html')

def test2(request):
    return render(request,'test2.html')