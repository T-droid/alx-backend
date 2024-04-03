#!/usr/bin/env python
"""defines implimentation of LIFO"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """impliments the fifo policy"""
    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assigns key value pair to a cache dictionary"""
        if key is None or item is None:
            pass
        else:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > self.MAX_ITEMS:
                last_item = self.keys.pop(-2)
                del self.cache_data[last_item]
                print("DISCARD: {}".format(last_item))

    def get(self, key):
        """gets the value of key"""
        if key:
            try:
                return self.cache_data[key]
            except Exception as e:
                return None
        return None
