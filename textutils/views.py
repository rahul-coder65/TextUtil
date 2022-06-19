# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params={'name' : 'rahul' , 'place' : 'deosia'}
    return render(request, 'index.html')
    # return HttpResponse("Home")
def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    #get the checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    # check which chechbox is on.
    if(charcount != "on" and removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps!="on"):
        return HttpResponse("Please select any operations and try again!")
    elif(charcount == "on" and (removepunc == "on" or newlineremover == "on" or extraspaceremover == "on" or fullcaps == "on")):
        return HttpResponse("For counting the characters. Please select only 'Character Counter' and try again!")
    elif (charcount == "on" and removepunc!="on" and newlineremover!="on" and extraspaceremover != "on" and fullcaps != "on"):
        params = {'purpose': 'Character Counter',
                  'analyzed_text': 'Total numbers of characters in given text is ' + str(len(djtext))}
        return render(request, 'analyze.html', params)
    else:
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed+=char;
        
            params = {'purpose' : 'Removed Punctuation', 'analyzed_text' : analyzed}
            djtext = analyzed
            # return render(request, 'analyze.html', params)
        if( fullcaps == "on"):
            analyzed = ""
            for char in djtext:
                analyzed+= char.upper();
            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
            djtext =analyzed
            # return render(request, 'analyze.html', params)
        if( newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != '\n' and char != '\r':
                    analyzed += char;
            params = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
            djtext = analyzed
            # return render(request, 'analyze.html', params)
        if (extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed += char;
            params = {'purpose': 'Extra Spaces Remover', 'analyzed_text': analyzed}
            # return render(request, 'analyze.html', params)
     
        
        return render(request, 'analyze.html', params)
