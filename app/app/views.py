 
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def generateoutput(request):
    receivetext = request.GET.get('text','default')
    punctuation = request.GET.get('punctuation','off')
    spelling = request.GET.get('spelling','off')
    upper = request.GET.get('upper','off')
    lower = request.GET.get('lower','off')


    if punctuation == 'on':
        generate = ""
        symbols = " .?!,:;-(){}[]‘“' "
        for char in receivetext:
            if char not in  symbols:
                generate = generate + char 
        params = {'Headline':'Generated Output','motive':'Punctuation removed Text:','text':generate}
        return render(request,'generateoutput.html',params)
    
    elif upper == 'on':
        generate = ""
        for char in receivetext:
            generate = generate + char.upper()
        params = {'Headline':'Generated Output','motive':'Text in Uppercase:','text':generate}
        return render(request,'generateoutput.html',params)

     
    elif lower == 'on':
        generate = ""
        for char in receivetext:
            generate = generate + char.lower()
        params = {'Headline':'Generated Output','motive':'Text in Lowercase:','text':generate}
        return render(request,'generateoutput.html',params)

    else :
        return render(request,'404.html')


