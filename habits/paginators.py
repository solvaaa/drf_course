from rest_framework.pagination import PageNumberPagination


class FivePagination(PageNumberPagination):
    page_size = 5