# I have created this file - omprakash
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #params = {'name':'Omprakash','place': "Ramgarh", 'collage':'Govt. Engineering Collage Bikaner'}
    return render(request, "index1.html")

def Analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    #check valuue of checkbox
    removepunc = request.POST.get('removepunc','off')

    uppercase = request.POST.get('uppercase','off')

    extraspaceremover = request.POST.get('extraspaceremover','off')

    charcounter = request.POST.get('charcounter','off')

    DigitRemover = request.POST.get('DigitRemover','off')

    newlineremover = request.POST.get('newlineremover','off')

    if djtext == "":
       return HttpResponse("Please Enter text")

    if(removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        
    if(uppercase == 'on'):
        analyzed=""
        for char in djtext:
            #if char not in punctuations:
            analyzed = analyzed + char.upper()
        djtext = analyzed
   
    if(extraspaceremover == 'on'):
        analyzed=" "
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        djtext = analyzed
        
    if(charcounter == 'on'):
        analyzed=""
        i = 0
        for index, char in enumerate(djtext):
            analyzed = analyzed + char
            if not(djtext[index] == " "):
                i = i+1
    if(DigitRemover == 'on'):
        analyzed = ""
        digit = '0123456789'
        for char in djtext:
            if char not in digit:
                analyzed = analyzed + char
        djtext = analyzed




    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if (char != '\n' and char !='\r'):
                analyzed = analyzed + char

    if (removepunc != 'on' and uppercase != 'on' and extraspaceremover != 'on' and DigitRemover != 'on' and newlineremover != 'on'):
        return HttpResponse('Please Check at least one box')

    params = {'purpose': "That's great", 'Analyzed_text': analyzed}
    return render(request, 'analyze1.html', params)
