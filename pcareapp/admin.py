from django.contrib import admin
from .models import Notification
from .models import Contact

# Register your models here.
admin.site.register(Notification)
admin.site.register(Contact)