from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .solver import solve
from .validate import validate

import json

@csrf_exempt
@require_http_methods(['POST'])
def solveTilepaint(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    res = solve(body['m'], body['n'], body['CG'], body['CC'], body['CR'])

    return JsonResponse(res)

@csrf_exempt
@require_http_methods(['POST'])
def validateTilepaint(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # print(body)
    res = validate(body['m'], body['n'], body['CG'], body['S'], body['CC'], body['CR'])
    # print(res)
    return JsonResponse(res)