from django.utils import timezone
from datetime import datetime, date
from django.shortcuts import redirect, render
from course_100days.models import StudySession
from datetime import datetime, date, timedelta
from django.contrib.admin.views.decorators import staff_member_required


COURSE_START = date(2026, 10, 4)
TOTAL_DAYS = 100


@staff_member_required
def index(request):
    today = timezone.localdate()
    day_number = (today - COURSE_START).days + 1
    day_number = min(day_number, TOTAL_DAYS)
    progress_percent = round(day_number / TOTAL_DAYS * 100)
    sessions = StudySession.objects.order_by('-clockin_time')
    total = sum((s.duration for s in sessions), timedelta())
    total_hours = round(total.total_seconds() / 3600, 1)
    
    context = {
        'is_clocked_in': 'clockin_time' in request.session,
        'sessions': StudySession.objects.order_by('-clockin_time'),
        'day_number': day_number,
        'sessions': sessions,
        'total_hours': total_hours,
        'progress_percent': progress_percent,
    }
    return render(request, 'index.html', context)


@staff_member_required
def clock_in(request):
    if request.method == 'POST':
        request.session['clockin_time'] = timezone.now().isoformat()
    return redirect('index')


@staff_member_required
def clock_out(request):
    if request.method == 'POST' and 'clockin_time' in request.session:
        start = datetime.fromisoformat(request.session.pop('clockin_time'))
        StudySession.objects.create(
            clockin_time=start,
            clockout_time=timezone.now(),
            learning=request.POST.get('learning', '').strip(),
        )
    return redirect('index')



