#!/usr/bin/env python3
""" Program module that takes two integer arguments page and page_size."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of (start_index, end_index) for pagination.

    Parameters:
        page (int): The page number, where the first page is page 1.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple (start_index, end_index) where:
        - start_index is the index of the first item on the page (0-indexed).
        - end_index is the index of the last item on the page (0-indexed).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
