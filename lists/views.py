from django.shortcuts import render
from django.views.generic import ListView
from .models import List
# Create your views here.
# def list(request):
#     lists = List.objects.all()
#     context = {
#         'lists': lists
#     }
#     return render(request, 'list.html', context)
class ListListView(ListView):
    model = List
    template_name = "index.html"