from django.http import JsonResponse
from django.views.generic import View


class HealthCheck(View):
    def get(self, request):
        data = {
            'success': True,
            'message': 'This is the a test view',
            'method': request.method,
        }
        return JsonResponse(data=data, status=200)
