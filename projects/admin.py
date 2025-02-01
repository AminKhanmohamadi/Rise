from django.contrib import admin
from .models import Tags , Customer , Project , Task
# Register your models here.

admin.site.register(Tags)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Task)