from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from universe.models import Write

# Create your views here.
def main(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('universe/board.html'))
    return render(request,'universe/main.html')

def board(request):
    write = Write.objects.all()
    return render(request, 'universe/board.html',{'write':write,})

def comment_page(request):
    write = Write.objects.all()
    return render(request, 'universe/comment_page.html',{'write':write,})

def post(request):
    write = Write()
    if request.method == 'POST':
        write.content = request.POST['content']
        write.save()
        return redirect('board')
    return render(request,'universe/post.html')