from django.utils import timezone
from datetime import datetime, date
from django.shortcuts import redirect, render
from course_100days.models import StudySession, Challenge
from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


COURSE_START = date(2026, 10, 4)
TOTAL_DAYS = 100


@login_required
def index(request):
    today = timezone.localdate()
    challenge = Challenge.objects.filter(owner=request.user).first()
    if challenge:
        day_number = (today - challenge.start_date).days + 1
        day_number = min(day_number, TOTAL_DAYS)
    else:
        day_number = 0
    progress_percent = round(day_number / TOTAL_DAYS * 100)
    sessions = StudySession.objects.filter(owner=request.user).order_by('-clockin_time')
    total = sum((s.duration for s in sessions), timedelta())
    total_hours = round(total.total_seconds() / 3600, 1)
    
    context = {
        'is_clocked_in': 'clockin_time' in request.session,
        'day_number': day_number,
        'sessions': sessions,
        'total_hours': total_hours,
        'progress_percent': progress_percent,
        'challenge': challenge,
    }
    return render(request, 'index.html', context)


@login_required
def clock_in(request):
    if request.method == 'POST':
        request.session['clockin_time'] = timezone.now().isoformat()
    return redirect('index')


@login_required
def clock_out(request):
    if request.method == 'POST' and 'clockin_time' in request.session:
        start = datetime.fromisoformat(request.session.pop('clockin_time'))
        StudySession.objects.create(
            owner=request.user,
            clockin_time=start,
            clockout_time=timezone.now(),
            learning=request.POST.get('learning', '').strip(),
        )
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def start_challenge(request):
    if request.method == 'POST':
        Challenge.objects.get_or_create(
            owner=request.user,
            defaults={'start_date': timezone.localdate()},
        )
    return redirect('index')



