from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)

    text1 = text.replace(" ", "")
    total_nospace_len = len(text1)

    wordList = text.split()
    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, 'result.html', {'total_len' : total_len, 'total_nospace_len' : total_nospace_len, "wordDict":wordDict.items})

def test(request):
    return render(request, 'test.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')