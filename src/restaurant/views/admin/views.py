import json

from django.contrib.auth.models import AnonymousUser
from django.views import View
from django.http import JsonResponse
from django.db import IntegrityError

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer
from restaurant.tasks import add_search_score
from user.permissions import IsSuperuser, IsRestaurantAdmin


# class AdminRestaurantView(View):
#     def _searializer(self, restaurant: Restaurant):
#         return {
#             'id': restaurant.id,
#             'name': restaurant.name,
#         }
#
#     def post(self, request):
#         if isinstance(request.user, AnonymousUser):
#             return JsonResponse({'message': 'user need to login'}, status=400)
#         body = json.loads(request.body.decode('utf-8'))
#         try:
#             restaurant = Restaurant(
#                 name=body.get('name'),
#                 address=body.get('address'),
#                 latitude=body.get('latitude'),
#                 longitude=body.get('longitude'),
#                 created_by=request.user
#             )
#             restaurant.save()
#             return JsonResponse({'data': self._searializer(restaurant)}, status=201)
#         except IntegrityError as e:
#             print(e)
#             return JsonResponse({'message': f'cannot create restaurant. reason: {e}'}, status=400)
#
#     def get(self, request):
#         if isinstance(request.user, AnonymousUser):
#             return JsonResponse({'message': 'user need to login'}, status=400)
#         return JsonResponse(data=[self._searializer(restaurant=res) for res in Restaurant.objects.all()], safe=False,
#                             status=200)


class AdminDRFRestaurantView(ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.filter()
    permission_classes = [IsAuthenticated, (IsSuperuser | IsRestaurantAdmin)]


class AdminRestaurantGetUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.filter()
    permission_classes = [IsAuthenticated, (IsSuperuser | IsRestaurantAdmin)]
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        obj: Restaurant = self.get_object()
        add_search_score.delay(res_id=obj.id)
        print(obj.pk)
        return super(AdminRestaurantGetUpdateDestroyView, self).retrieve(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     obj: Restaurant = self.get_object()
    #     obj.is_active = False
    #     obj.status = 'inactive'
    #     obj.save()
    #     return Response(data=self.get_serializer(obj).data, status=status.HTTP_200_OK)



