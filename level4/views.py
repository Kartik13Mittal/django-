from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'level4/index.html',context=context_dict)

def other(request):
    return render(request,'level4/other.html')    

def relative(request):
    return render(request,'level4/relativeurl.html')