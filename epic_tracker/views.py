from django.shortcuts import render


# Create your views here.
from epic_tracker.models.epic_status import EpicStatus


def epic_dashboard(request):
    epicList = EpicStatus.objects.all()

    return render(request, 'epicDashboard.html', {'epicList' : epicList})
