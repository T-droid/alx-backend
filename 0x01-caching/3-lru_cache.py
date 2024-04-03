#!/usr/bin/env python3
"""implimentation of LRU"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """impliments LRU caching policy"""
    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assigns key value to cache dictionary"""
        if key is None or item is None:
            pass
        else:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > self.MAX_ITEMS:
                least_recent = self.keys.pop(0)
                del self.cache_data[least_recent]
                print("DISCARD: {}".format(least_recent))

    def get(self, key):
        """gets the value of key"""
        if key:
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)

            try:
                return self.cache_data[key]
            except Exception as e:
                return None
        return None
