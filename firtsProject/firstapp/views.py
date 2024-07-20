from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Profile

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

class CarListView(TemplateView):
  template_name = "firstapp/car_list.html"

  def get_context_data (self):
      car_list = [
        {"title":"ford"},
        {"title":"audi"},
        {"title":"chevrolet"}
    ]
      return {
      "car_list": car_list
    }

def view(request, *args, **kwargs):
  print(args)
  print(kwargs)
  return HttpResponse("")

def test(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def authorView(request, *args, **kwargs):
  print(kwargs['author_id'])
  getAuthor = Author.objects.get(id=kwargs['author_id'])
  getProfile = Profile.objects.get(id=kwargs['author_id'])

  return HttpResponse(f"Author: {getAuthor.name} - website: {getProfile.website} - bio {getProfile.bio}")


