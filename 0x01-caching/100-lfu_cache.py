#!/usr/bin/env python3
"""
Defines a LFUCache class that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Defines methods to cache data using LFU algorithm
    """

    def __init__(self):
        """
        Initializes the LFU cache instance
        """
        super().__init__()
        self.freq = {}
        self.fc = {}

    def put(self, key, item):
        """
        Adds an item to the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.freq[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                if len(least_freq_keys) == 1:
                    discarded_key = least_freq_keys[0]
                else:
                    min_fc = min(
                        self.fc.get(k, 0) for k in least_freq_keys
                    )
                    discarded_key = [
                        k for k, v in self.fc.items() if v == min_fc
                    ][0]
                del self.cache_data[discarded_key]
                del self.freq[discarded_key]
                del self.fc[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.freq[key] = 1
            self.fc[key] = 0

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.freq[key] += 1
            self.fc[key] += 1
            return self.cache_data[key]
        return None
