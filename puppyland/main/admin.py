from django.contrib import admin
from .models import Dog # add this

class DogAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'dog_breed','dog_gender','dog_weight','dog_age',
    'img' )
admin.site.register(Dog, DogAdmin)