from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'home':'current'}
    return render(request, 'webapp/home.html',context)

#view to show about us page 
def aboutus(request):
    context = {'about':'current'}
    return render(request, 'webapp/about.html',context)
#contact us page 
def contactus(request):
    
    context = {'contactss':'current'}
    return render(request, 'webapp/contact.html',context)