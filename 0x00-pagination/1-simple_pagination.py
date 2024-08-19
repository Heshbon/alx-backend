#!/usr/bin/env python3
""" Program module that takes two integer arguments page and page_size."""
import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []  # Empty list
        return dataset[start_index:end_index]
