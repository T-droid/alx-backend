#!/usr/bin/env python3
""" a class to define the FIFO policy"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """impliments the fifo caching policy"""
    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assigns key value pair to dictionary cache"""
        if key is None or item is None:
            pass

        else:
            if key not in self.keys:
                self.keys.append(key)

            self.cache_data[key] = item

            if len(self.keys) > self.MAX_ITEMS:
                oldest = self.keys.pop(0)
                del self.cache_data[oldest]
                print("DISCARD: {}".format(oldest))

    def get(self, key):
        """gets the value of key"""
        if key:
            try:
                return self.cache_data[key]
            except Exception as e:
                return None
        return None
