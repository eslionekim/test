from django.shortcuts import render

from universe.models import Write

# Create your views here.
def main(request):
    return render(request,'universe/main.html')

def board(request):
    write = Write.objects.all()
    return render(request, 'universe/board.html',{'write':write,})

def comment_page(request):
    write = Write.objects.all()
    return render(request, 'universe/comment_page.html',{'write':write,})