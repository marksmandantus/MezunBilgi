from django.shortcuts import render

def is_ilanlari(request):
    return render(request, 'is_ilanlari.html')

def web_gelistirici(request):
    return render(request, 'web_gelistirici.html')
