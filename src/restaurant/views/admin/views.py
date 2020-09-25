import json

from django.contrib.auth.models import AnonymousUser
from django.views import View
from django.http import JsonResponse
from django.db import IntegrityError

from restaurant.models import Restaurant


class AdminRestaurantView(View):
    def _searializer(self, restaurant: Restaurant):
        return {
            'id': restaurant.id,
            'name': restaurant.name,
        }

    def post(self, request):
        if isinstance(request.user, AnonymousUser):
            return JsonResponse({'message': 'user need to login'}, status=400)
        body = json.loads(request.body.decode('utf-8'))
        try:
            restaurant = Restaurant(
                name=body.get('name'),
                address=body.get('address'),
                latitude=body.get('latitude'),
                longitude=body.get('longitude'),
                created_by=request.user
            )
            restaurant.save()
            return JsonResponse({'message': 'restaurant created'}, status=201)
        except IntegrityError as e:
            print(e)
            return JsonResponse({'message': f'cannot create restaurant. reason: {e}'}, status=400)

    def get(self, request):
        if isinstance(request.user, AnonymousUser):
            return JsonResponse({'message': 'user need to login'}, status=400)
        return JsonResponse(data=[self._searializer(restaurant=res) for res in Restaurant.objects.all()], safe=False,
                            status=200)
