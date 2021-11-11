from django.contrib import admin
from .models import Agents , User, Leads
# Register your models here.

admin.site.register(Leads)
admin.site.register(User)
admin.site.register(Agents)