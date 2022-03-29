from django.shortcuts import render


# Create your views here.
def error_404(request, exception):
    return render(request, 'error/error_404.html')


def error_400(request, exception):
    return render(request, 'error/error_400.html')


def error_403(request, exception):
    return render(request, 'error/error_403.html')


def error_500(request):
    return render(request, 'error/error_500.html')
