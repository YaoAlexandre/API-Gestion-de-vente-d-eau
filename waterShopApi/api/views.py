from django.http import JsonResponse;

def getRoute(request):
    routes = [
        {
            'Endpoint':  '/water/',
            'method': 'GET',
            'body': None,
            'description': 'returns an array of waters '
        }
    ]
    return JsonResponse(routes, safe=False)