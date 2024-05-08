from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from  django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def course_chat_room(request, course_id):
    # course = get_object_or_404(request.user.courses)
    try:
        course = request.user.courses_joined.get(id=course_id)
    except:
        return HttpResponseForbidden("Something is wrong!!!!!")
    return render(request, 'chat/room.html',{'course':course})

