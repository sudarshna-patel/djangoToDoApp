from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    all_items = None
    if (request.method == 'POST'):
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = ListForm()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added tTo The List!'))
    else:
        all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def delete(request, id):
    item = List.objects.get(id=id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def cross_off(request, id):
    item = List.objects.get(id=id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, id):
    item = List.objects.get(id=id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, id):
    if request.method == 'POST':
        item = List.objects.get(id=id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(id=id)
        return render(request, 'edit.html', {'item': item})