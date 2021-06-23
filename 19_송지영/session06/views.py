from django.shortcuts import render

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    blank_no = len(text.replace(" ",""))
    split_list = text.split(" ")
    return render(request, 'result.html', {
        'text' : text,
        'total_len' : total_len,
        'blank_no' : blank_no,
        'split_list' : split_list,
    })

def test(request):
    return render(request, 'test.html')

def test1(request):
    Name = request.GET['name']
    return render(request, 'test1.html',{'Name' : Name})

def test2(request):
    return render(request, 'test2.html')