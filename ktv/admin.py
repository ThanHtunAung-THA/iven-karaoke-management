from django.contrib import admin
from .models import Room, Customer, Song, Booking, Payment

# Register your models here.
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Song)
admin.site.register(Booking)
admin.site.register(Payment)

