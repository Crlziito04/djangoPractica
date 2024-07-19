from django.shortcuts import render

# Create your views here.
def my_view(request):
  car_list = [
    {"title":"ford"},
    {"title":"audi"},
    {"title":"chevrolet"}
  ]
  context = {
    "car_list": car_list
  }
  return render(request, "firstapp/car_list.html",context)