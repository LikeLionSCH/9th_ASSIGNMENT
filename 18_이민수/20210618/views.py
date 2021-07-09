from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    null_len = len(text.replace(" ",""))
    word_list = text.split()
    return render(request, 'result.html', {
        'total_len' : total_len,
        'null_len' : null_len,
        'word_list' : word_list,
        })

def register(request):
    return render(request, 'register.html', {'first_name':'John'})

def count(request):
    return render(request, 'count.html')