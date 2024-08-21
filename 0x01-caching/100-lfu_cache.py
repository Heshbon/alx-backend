#!/usr/bin/env python3
""" The module for LFU Caching"""
from base_caching import BaseCaching
from time import time


class LFUCache(BaseCaching):
    """ LFUCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initialize the LFU Cache"""
        super().__init__()
        self.usage_counts = {}
        self.usage_order = {}

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_counts[key] += 1
            self.usage_order[key] = self._current_time()
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.usage_counts.values())
                lfu_keys = [a for a, b in self.usage_counts.items(
                    ) if b == min_freq]

                lru_key = min(lfu_keys, key=lambda a: self.usage_order[a])
                del self.cache_data[lru_key]
                del self.usage_counts[lru_key]
                del self.usage_order[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.usage_counts[key] = 1
            self.usage_order[key] = self._current_time()

    def get(self, key):
        """ Retrieves the value associated with key from self.cache_data"""
        if key is None or key not in self.cache_data:
            return None

        self.usage_counts[key] += 1
        self.usage_order[key] = self._current_time()
        return self.cache_data[key]

    def _current_time(self):
        """ The current time"""
        return int(time() * 1000)
