from django.shortcuts import render

def count(request):
    return render(request,'count.html')

def results(request):
    text=request.POST['text']
    total_len=len(text)
    
    #letterCount = len(text.replace(" ", ""))
    letterCount=0
    for letter in text:
        if letter!=' ' and letter != '\n':
            letterCount+=1
    text=text.split()
    return render(request, 'results.html', {'text':text, 'total_len':total_len, 'letterCount':letterCount})

def test(request):
    return render(request, 'test.html')
def test1(request):
    return render(request, 'test1.html')
def test2(request):
    return render(request, 'test2.html')