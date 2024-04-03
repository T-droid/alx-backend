#!/usr/bin/env python3
"""this is a basic cache system with a dictionary"""
from base_caching import BaseCaching
from numpy import Infinity


class BasicCache(BaseCaching):
    """impliments a basic caching system"""
    MAX_ITEMS = Infinity

    def __init__(self):
        """initialisation part"""
        super().__init__()

    def put(self, key, item):
        """assigns to dictionary key value"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        """gets the value of the key"""
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except Exception as e:
            return None

