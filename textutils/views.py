# I have created ths file-- Banshika Badkul


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercount = request.POST.get('charactercount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char != '\r':
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if charactercount == "on":
        count = 0
        for char in djtext:
            count += 1
        params = {'purpose': 'Character Count', 'analyzed_text': count}

    if(removepunc != "on" and fullcaps !="on" and newlineremover !="on" and extraspaceremover != "on" and charactercount !="on"):
        return HttpResponse("ERROR \n please choose any option")

    return render(request, 'analyze.html', params)
