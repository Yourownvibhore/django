from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request, 'index1.htm',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.htm')
    # return HttpResponse("this is about")
def services(request):
    return render(request, 'services.htm')
    # return HttpResponse("this is services")
def contact(request):
    return render(request, 'contact.htm')
    # return HttpResponse("contact")
