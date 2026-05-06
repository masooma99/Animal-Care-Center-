from django.shortcuts import render


# Create your views here.
def intro_page(request):
    return render(request, "intro_page.html")
