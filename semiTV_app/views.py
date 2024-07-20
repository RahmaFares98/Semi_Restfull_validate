from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from . import models
#to show all shows in networks 
def shows_list(request):
    shows = models.Show.objects.all()
    return render(request, 'show_list.html', {'shows': shows})
# to add a new show
def show_new(request):
    if request.method == 'POST': # if it post get data from users 
        errors =models.Show.objects.check_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else :
            title = request.POST.get('title')
            network = request.POST.get('network')
            release_date = request.POST.get('release_date')
            description = request.POST.get('description')
            show=models.addshow(title=title,network=network,release_date=release_date,description=description)
            print (show)
            return redirect('/')


    
    # If GET request or validation errors, render the show_new.html template
    return render(request, 'show_new.html')

#to show details of specific show
def show_det(request,id):
        show_details = get_object_or_404(models.Show, id=id)  # Retrieve Show object by id or return 404 if not found
        print(show_details)  # Print show_details to console for debugging
        return render(request, 'show_details.html', {'show_details': show_details})

#to edit our show
def show_edit(request, id):
    all_shows = models.Show.objects.all()
    show = get_object_or_404(models.Show, id=id)
    
    if request.method == 'POST':
        # Validate form data using ShowManager.check_validator method
        errors = models.Show.objects.check_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            # Return to the edit form with validation errors
            return render(request, 'edit_show.html', {'show': show, 'all_shows': all_shows})
        # Update the fields of the Show object based on POST data
        show.title = request.POST.get('title', show.title)
        show.description = request.POST.get('description', show.description)
        show.release_date = request.POST.get('release_date', show.release_date)
        show.network = request.POST.get('network', show.network)
        # Check if title is unique
        if show.title != request.POST.get('title') and models.Show.objects.filter(title=show.title).exists():
            messages.error(request, 'Title must be unique.')
            return render(request, 'edit_show.html', {'show': show, 'all_shows': all_shows})
        # Save the updated Show object
        show.save()
        # Redirect to the show_detail view with the updated show's id
        return redirect('show_detail', id=id)
    # Render the edit form template with the Show object and all shows
    return render(request, 'edit_show.html', {'show': show, 'all_shows': all_shows})

#do you want to delete ? confirm !
def confirm_delete(request, id):
    show = get_object_or_404(models.Show, id=id)
    return render(request, 'confirm_delete.html', {'show': show})

#after confirm ,Please Delete.
def show_delete(request):
    if request.method == 'POST':
        id = request.POST.get("cid")
        show=get_object_or_404(models.Show,id=id)
        show.delete()
    return redirect('/')  # Redirect to home 
