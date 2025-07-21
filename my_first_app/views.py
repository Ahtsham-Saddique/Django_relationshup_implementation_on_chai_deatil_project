from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import App
# Create your views here.
def all_temp(request):
    chais=App.objects.all()
    return render(request,'my_first_app/app.html',{'chais':chais})
def chai_details(request,chai_id):
    chai = get_object_or_404(App,pk=chai_id)
    return render(request, "my_first_app/chai_details.html", {'chai': chai})
