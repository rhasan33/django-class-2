import json

from django.views import View
from django.http import JsonResponse
from django.conf import settings

import jwt

from user.models import User


class LoginView(View):
    @staticmethod
    def _serializer(user: User):
        return {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'groups': [group.name for group in user.groups.all()]
        }

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.get(username=body.get('username'))
            if not user.check_password(raw_password=body.get('password')):
                return JsonResponse({'message': 'invalid password'}, status=400)
            user_data = self._serializer(user=user)
            token = jwt.encode(payload=user_data, key=settings.SECRET_KEY, algorithm='HS256')
            return JsonResponse({'access_token': token.decode('utf-8')}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': 'cannot find user'}, status=404)
