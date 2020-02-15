from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import Room, RoomMember
import json

def go_to_home(request):
	return render(request, 'account.html')

def create_room(request):
	room_no = request.POST.get('room_no_c')
	user = request.session['email']
	room = Room.objects.filter(room_no=room_no)

	if len(room) == 0:
		Room.objects.create(room_no=room_no, owner=user)
		RoomMember.objects.create(room_no=room_no, member=user, isAuthorized='Y')
		return render(request, 'account.html')

	else:
		return render(request, 'room_error.html', {'message': 'Room already exists!'})

def delete_room(request):
	room_no = request.POST.get('room_no_d')
	user = request.session['email']

	room = Room.objects.filter(room_no=room_no)

	if len(room) == 0:
		return render(request, 'room_error.html', {'message': 'Room does not exist'})
	else:
		if user != room[0].owner:
			return render(request, 'room_error.html', {'message': 'You are not authorized to delete the room'})

		else:
			room.delete()
			return render(request, 'account.html')

def join_room(request):
	room_no = request.POST.get('room_no_j')
	user = request.session['email']

	room = Room.objects.filter(room_no=room_no)

	if len(room) == 0:
		return render(request, 'room_error.html', {'message': 'Room does not exist'})
	else:
		if user == room[0].owner:
			isOwner = True
			return render(request, 'room.html', {'room_no': room_no, 'isOwner': isOwner})
		else:
			isOwner = False

			member = RoomMember.objects.filter(room_no=room_no, member=user)

			if len(member) == 0:
				RoomMember.objects.create(room_no=room_no, member=user, isAuthorized='N')
				return render(request, 'room_error.html', {'message': 'You are not a member of this room, but your request to join the room has been sent to the owner!'})
			else:
				if member[0].isAuthorized != 'Y':
					return render(request, 'room_error.html', {'message': 'Your request to join the room has not been approved yet! Try to contact the owner!'})
				else:
					return render(request, 'room.html', {'room_no': room_no, 'isOwner': isOwner})

def pending_request(request):
	user = request.session['email']
	req = json.loads(request.body.decode())
	room_no = req['room_no']

	members = RoomMember.objects.filter(room_no=room_no, isAuthorized='N')
	ret = [item.member for index, item in enumerate(members)]

	rdata = {
		'data': ret
	}

	return JsonResponse(rdata)

def approve_request(request):
	user = request.session['email']
	req = json.loads(request.body.decode())
	room_no = req['room_no']
	email = req['email']

	RoomMember.objects.filter(room_no=room_no, member=email).update(isAuthorized='Y')

	rdata = {
		'status_code': 200,
	}

	return JsonResponse(rdata)