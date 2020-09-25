from typing import Union

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'

    def _get_next_page(self) -> Union[int, None]:
        if not self.page.has_next():
            return None
        page_number: int = self.page.next_page_number()
        return page_number

    def _get_previous_page(self) -> Union[int, None]:
        if not self.page.has_previous():
            return None
        page_number: int = self.page.previous_page_number()
        return page_number

    def get_paginated_response(self, data):
        return Response({
            'meta_data': {
                'count': self.page.paginator.count,
                'page_size': self.get_page_size(self.request),
                'next': self._get_next_page(),
                'previous': self._get_previous_page(),
            },
            'data': data
        })
