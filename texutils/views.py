from typing import Text
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")


def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {"purpose":"Removing Punctuation","analyzed_text":analyzed}
        return render(request,'analyze.html',params)

    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()

        params = {"purpose":"Full Capitalize","analyzed_text":analyzed}
        return render(request,'analyze.html',params)
    
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    # Analyze the text

        return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):

            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {"purpose":"newlineremover","analyzed_text":analyzed}
        return render(request,'analyze.html',params)  

    if charcount=="on":
        analyzed = ""
        for char in djtext:
            
            analyzed =analyzed + char
            text = len(analyzed)
           
        params = {"purpose":"Character Counter","text":f"The total number of character in your string is  {text}"}
        return render(request,'analyze.html',params) 

    else:
        return HttpResponse("error")
    

