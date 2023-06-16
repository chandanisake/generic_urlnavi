from django.shortcuts import render

# Create your views here.
def pinky(request):
    return render(request,'pinky.html')

def chandu(request):
    return render(request,'chandu.html')

