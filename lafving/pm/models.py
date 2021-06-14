from django.db import models
import datetime as dt

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    goal = models.TextField(max_length=255)
    drive_folder = models.URLField()
    paying = models.BooleanField()
    def __str__(self):
        return self.client_name

    class meta:
        abstract = True

class Project(Client):
    project_name = models.CharField(max_length=100)
    def __str__(self):
        return self.project_name

class Deliverable(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE
    )
    deliverable_name = models.CharField(max_length=100)
    deadline = models.DateField()
    delivered = models.BooleanField()
    
    def __str__(self):
        return ' — '.join([
            self.project.project_name,
            self.deliverable_name,
        ])
        # if delivered: ... create new Deliverable with deadline 

    # resource = models.ManyToManyField(

    # )
# class RecurringDeliverable(Deliverable):


class Session(models.Model):
    deliverable = models.ForeignKey(
        'Deliverable',
        on_delete=models.CASCADE
    )
    date = models.DateField(default=dt.date.today)
    start = models.TimeField(default=dt.datetime.now().replace(second=0, microsecond=0), help_text='Hit Save and Continue Editing. Then hit save when done to stop the session.')
    paid = models.BooleanField(default=False)
    stop = models.DateTimeField(auto_now=True)
    working = models.ManyToManyField(
        'Step',
        related_name = 'sessions',
        related_query_name = 'session'
    )
    def __str__(self):
        return ' '.join([
            self.deliverable.project.project_name,
            self.deliverable.deliverable_name, 
            self.date.isoformat(),
            str('Session #: ' + str(self.id))
        ])
    # On creation session will ask what step is working
    # Set up Pause model with many to one relationship

class Step(models.Model):
    description = models.CharField(max_length=100)
    time_estimate = models.DurationField()
    done = models.BooleanField()
    deliverable = models.ForeignKey(
        'Deliverable',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.description

# class Resource(models.Model):
#     LINK = 'LK'
#     FILE = 'FL'
#     CONTACT = 'CT'
#     APPLICATION = 'AP'
    
#     RESOURCE_TYPES = [
#         (LINK, 'Web Page'),
#         (FILE, 'File'),
#         (CONTACT, 'Contact'),
#         (APPLICATION, 'Application')
#     ]
#     resource_type = models.CharField(
#         max_length = 2,
#         choices = RESOURCE_TYPES,
#         default = LINK,
#     )

#     resource_name = models.CharField(max_length=100)