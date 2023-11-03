from rest_framework.pagination import PageNumberPagination


class FivePagination(PageNumberPagination):
    '''Paginates by 5'''
    page_size = 5
