from django.contrib import admin
from .models import tempItems

@admin.register(tempItems)
class GameAdmin(admin.ModelAdmin):
	list_display = ('id','name','img')
# Register your models here.
