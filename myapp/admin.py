from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from myapp.models import Contact


admin.site.register(Contact)


