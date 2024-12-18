from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Room, Booking, Song, Customer
from django.utils.timezone import now

# Create your views here.

# Room List
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'ktv/room_list.html', {'rooms': rooms})

# Book Room
def book_room(request, room_id):
    if request.method == 'POST':
        customer = request.user.customer
        room = get_object_or_404(Room, id=room_id)
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        booking = Booking.objects.create(
            customer=customer,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return JsonResponse({'success': True, 'booking_id': booking.id})

# Song List
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'ktv/song_list.html', {'songs': songs})

