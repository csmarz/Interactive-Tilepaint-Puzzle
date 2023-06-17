from django.http import JsonResponse, response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .solver import solve
from .validate import validate
import os

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


@csrf_exempt
@require_http_methods(['GET'])
def getTC(request, id):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'members', 'static', 'TC', f'{id}_tc.in')
    f = open(file_path)

    res = []

    m, n = map(int, f.readline().strip().split())
    res.append([m, n])
    res.append(list(map(int, f.readline().strip().split())))
    res.append(list(map(int, f.readline().strip().split())))
    
    for _ in range(m):
        res.append(list(map(int, f.readline().strip().split())))

    f.close()
    
    return JsonResponse({"res": res})