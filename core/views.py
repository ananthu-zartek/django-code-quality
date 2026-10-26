import json

from django.http import HttpRequest, JsonResponse


def health(request):
    return JsonResponse({"status": "ok"})










def checks(request: HttpRequest) -> JsonResponse:
    payload: dict[str, str] = {"status": "ok", "checks": 1}
    return JsonResponse(payload)
