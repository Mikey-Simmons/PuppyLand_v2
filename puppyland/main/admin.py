from django.contrib import admin
from .models import Dog, Customer # add this

class DogAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'dog_breed','dog_gender','dog_weight','dog_age',
    'img' )
admin.site.register(Dog, DogAdmin)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','dog','email','phone','dogs_owned','description','reason_why','occupataion')
admin.site.register(Customer,CustomerAdmin)