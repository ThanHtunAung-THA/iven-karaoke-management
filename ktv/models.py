from django.db import models
from django.contrib.auth.models import User

# Room Model
class Room(models.Model):
    name = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50, choices=[('VIP', 'VIP'), ('Regular', 'Regular')])
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

# Song Model
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.DurationField()

    def __str__(self):
        return self.title

# Booking Model
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def calculate_price(self):
        duration = (self.end_time - self.start_time).total_seconds() / 3600
        self.total_price = duration * self.room.price_per_hour
        return self.total_price

    def save(self, *args, **kwargs):
        self.calculate_price()
        super().save(*args, **kwargs)

# Payment Model
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Card', 'Card')])

    def __str__(self):
        return f"Payment for {self.booking}"

