from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to home page via ..mgmt/views.py")