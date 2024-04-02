#!/usr/bin/env python3
"""
Defines a LIFOCache class that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines methods to cache data using LIFO algorithm
    """

    def __init__(self):
        """
        Initializes the LIFO cache instance
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Adds an item to the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
