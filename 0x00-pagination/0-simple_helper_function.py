#!/usr/bin/env python3
"""defines index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple showing the start index and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
