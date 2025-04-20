from django.shortcuts import render


def mp(request):
    return render(request, 'main_page/index.html')
