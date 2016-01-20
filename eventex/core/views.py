from django.shortcuts import render


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo' : 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo' : 'http://hbn.link/turing-pic'}
    ]
    context = {'speakers': speakers}
    return render(request, 'index.html', context)
