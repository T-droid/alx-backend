#!/usr/bin/env python3
"""definition of Server and index_range"""
import csv
import math
from typing import List


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
        """gets page"""
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"
        data = self.dataset()
        start, end = index_range(page, page_size)
        filtered_data = []

        filtered_data = data[start: end]
        return [] if not filtered_data else filtered_data


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple showing the start index and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
