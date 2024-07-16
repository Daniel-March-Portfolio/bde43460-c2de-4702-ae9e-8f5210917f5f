from django.http import HttpResponse

from Receipt.management.commands.calculate_receipts import Command


def run_receipts_calculating(request):
    if request.method != "GET":
        return HttpResponse(status=405)
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    Command().handle()
    return HttpResponse(status=200)
