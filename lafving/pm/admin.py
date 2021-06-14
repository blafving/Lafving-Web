from django.contrib import admin
from .models import Client, Project, Deliverable, Session, Step

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Deliverable)
admin.site.register(Session)
admin.site.register(Step)

# Register your models here.
