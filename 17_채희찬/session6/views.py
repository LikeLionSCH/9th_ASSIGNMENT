from django.shortcuts import render

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    except_blank = len(text.replace(" ",""))
    return render(request, 'result.html', {
        'total_len' : total_len,
        'except_blank' :  except_blank,
        'words' : text.split(" "),
    })

def test(request):
    return render(request, 'test.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')
