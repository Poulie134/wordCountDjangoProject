from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
def count(request):
    fullText = request.GET['fullText']
    wordList=fullText.split()
    countLetters = 0
    wordDictionary = {}
    for i in wordList:
        countLetters += len(i)
        if i in wordDictionary:
            wordDictionary[i] += 1
        else:
            wordDictionary[i] = 1
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fullText':fullText,'countWords':len(wordList),'countLetters':countLetters,'sortedWords':sortedWords})
def about(request):
    return render(request, 'about.html')