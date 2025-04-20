from django.shortcuts import render

def first_page(request):
    return render(request, 'register_pages/first_page.html')

def second_page(request):
    return render(request, 'register_pages/second_page.html')