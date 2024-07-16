from django.http import HttpResponse
from django.shortcuts import redirect

from Progress.models import Progress
from Receipt.management.commands.calculate_receipts import Command


def run_receipts_calculating(request):
    if request.method != "GET":
        return HttpResponse(status=405)
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    progress_uuid = Progress.objects.create(target_value=1).uuid
    Command().handle(progress_uuid=progress_uuid)
    return redirect(f"/api/progress/{progress_uuid}")
