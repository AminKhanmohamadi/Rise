from django.contrib import admin
from .models import Tags  , Project , Task
# Register your models here.

admin.site.register(Tags)
admin.site.register(Project)
admin.site.register(Task)