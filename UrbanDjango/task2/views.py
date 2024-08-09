from django.shortcuts import render


# Create your views here.
def class_view(request):
    return render(request, "class_view.html")


def func_view(request):
    return render(request, "func_view.html")
