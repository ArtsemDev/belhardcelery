from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from .tasks import my_task


def index(request: HttpRequest) -> JsonResponse:
    my_task.delay()
    return JsonResponse({'status': 'OK'})
