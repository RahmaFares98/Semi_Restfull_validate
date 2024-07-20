from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def check_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        try:
            release_date = postData.get('release_date')
            if release_date:
                release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
                if release_date >= datetime.now().date():
                    errors["release_date"] = "Release date should be in the past"
        except ValueError:
            errors["release_date"] = "Invalid date format"
        return errors
    
#to define class called show
class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()    # add this line!
    
    #return Updated date 
    def __str__(self):
        return self.title
    
#create show :
def addshow(title,network,release_date,description):
    show= Show.objects.create(title=title,network=network,release_date=release_date,description=description)
    return show
