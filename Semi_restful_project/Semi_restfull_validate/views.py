from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Show
from .forms import ShowForm  # Adjust if you have a forms.py file

def shows_list(request):
    shows = Show.objects.all()
    return render(request, 'show_list.html', {'shows': shows})

def show_detail(request, id):
    show = get_object_or_404(Show, pk=id)
    return render(request, 'show_detail.html', {'show': show})

def new_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shows')
    else:
        form = ShowForm()
    return render(request, 'new_show.html', {'form': form})

def create(request):  # Ensure this matches the name in urls.py
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shows')
    else:
        form = ShowForm()
    return render(request, 'new_show.html', {'form': form})

def edit_show(request, id):
    show = get_object_or_404(Show, pk=id)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            show = form.save()
            return redirect('show_detail', id=show.id)
    else:
        form = ShowForm(instance=show)
    return render(request, 'show_form.html', {'form': form, 'show': show})


def update_show(request, id):
    show = get_object_or_404(Show, id=id)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('/shows')
    else:
        form = ShowForm(instance=show)
    return render(request, 'edit_show.html', {'form': form, 'show': show})

def destroy_show(request, id):
    show = get_object_or_404(Show, id=id)
    if request.method == 'POST':
        show.delete()
        return redirect('/shows')
    return render(request, 'confirm_delete.html', {'show': show})

def check_unique_title(request):
    title = request.POST.get('title', None)
    data = {
        'is_taken': Show.objects.filter(title=title).exists()
    }
    return JsonResponse(data)
