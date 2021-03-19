from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html') # pass html page as a string otherwise it (show function object has no attribut html) 

def analyze(request):
    textareavalue=request.GET.get('textarea','write anything')
    punctuation_remove=request.GET.get('punctuation','off')
    capitalize=request.GET.get('capitalize','off')
    newline_remove=request.GET.get('newline_remove','off')
    char_count=request.GET.get('char_count','off')
    space_remove=request.GET.get('space_remove','off')
    # return HttpResponse(textareavalue+" "+checkboxvalue) 
    if punctuation_remove=='on':
        puncuation_list='''!()-[]{};:'"/\,.<>?@#$%^&*_~'''
        analyzed=""
        for char in textareavalue:
            if char not in puncuation_list:
                analyzed+=char
        params={'purpose':'remove puncuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif capitalize=='on':
        result=""
        for char in textareavalue:
            result+=char.upper()
        params={'purpose':"Capatilized word",'analyzed_text':result}
        return render(request,'analyze.html',params)
    elif space_remove=='on':
        result=textareavalue.replace("  "," ")
        params={'purpose':"space remove",'analyzed_text':result}
        return render(request,'analyze.html',params)
    elif char_count=='on':
        result=0
        for char in textareavalue:
            if char==' ':
                pass
            else:
                result+=1
        params={'purpose':"Count character",'analyzed_text':result}
        return render(request,'analyze.html',params)
    elif newline_remove=='on':
        result=""
        for char in textareavalue:
            if char == '\n':
                pass
            else:
                result+=char 
        params={'purpose':"newline remove",'analyzed_text':result}
        return render(request,'analyze.html',params)
    else:
        params={'purpose':"simpe text display",'analyzed_text':textareavalue}
        return render(request,'analyze.html',params)






