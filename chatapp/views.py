from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'chat.html', {})
def room(request,room):

    return render(request,'room.html',{})