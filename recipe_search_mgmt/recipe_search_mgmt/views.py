from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the overall homepage via ..mgmt/views.py")

