#!/usr/bin/env python3
"""
Defines a LRUCache class that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Defines methods to cache data using LRU algorithm
    """

    def __init__(self):
        """
        Initializes the LRU cache instance
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Adds an item to the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
