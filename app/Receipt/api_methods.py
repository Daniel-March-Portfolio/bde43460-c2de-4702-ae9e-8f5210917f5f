from datetime import date

from django.http import HttpResponse
from django.shortcuts import redirect

from Progress.models import Progress
from Receipt.management.commands.calculate_receipts import Command


def run_receipts_calculating(request):
    if request.method != "GET":
        return HttpResponse(status=405)
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    current_data = date.today()
    month = request.GET.get("month") or current_data.month
    year = request.GET.get("year") or current_data.year
    date_for_calculating = date(year=int(year), month=int(month), day=1)
    progress_uuid = Progress.objects.create(target_value=1).uuid
    Command().handle(progress_uuid=progress_uuid, date_for_calculating=date_for_calculating)
    return redirect(f"/api/progress/{progress_uuid}")
