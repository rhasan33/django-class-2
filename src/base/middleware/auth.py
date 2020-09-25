from django.conf import settings
from django.http import JsonResponse

import jwt

from user.models import User


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token_header: str = request.headers.get('authorization')
        if token_header:
            token = token_header.split(' ')[1]
            try:
                data = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256', verify=True)
                try:
                    user = User.objects.get(username=data['username'])
                    setattr(request, 'user', user)
                    setattr(request, 'group', user.groups.all())
                except User.DoesNotExist:
                    return JsonResponse({'message': f'cannot find user'}, status=404)
            except Exception as err:
                return JsonResponse({'message': f'cannot decode token. reason: {err}'}, status=400)
        response = self.get_response(request)
        return response
