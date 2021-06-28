from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone


def re_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 're_list.html', {'restaurants': restaurants})

def re_detail(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    return render(request, 're_detail.html', {'restaurant': restaurant})

def re_new(request):
    return render(request, 're_new.html')

def re_create(request):
    new_restaurant = Restaurant()
    new_restaurant.name = request.POST['name']
    new_restaurant.address = request.POST['address']
    new_restaurant.author = request.POST['author']
    new_restaurant.body = request.POST['body']
    new_restaurant.date = timezone.now()
    new_restaurant.save()
    return redirect('re_list')

def re_edit(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    return render(request, 're_edit.html', {'restaurant': restaurant})

def re_update(request, id):
    update_restaurant = Restaurant.objects.get(pk=id)
    update_restaurant.name = request.POST['name']
    update_restaurant.address = request.POST['address']
    update_restaurant.author = request.POST['author']
    update_restaurant.body = request.POST['body']
    update_restaurant.save()
    return redirect('re_detail', update_restaurant.id)

def re_delete(request, id):
    delete_restaurant = Restaurant.objects.get(pk=id)
    delete_restaurant.delete()
    return redirect('re_list')