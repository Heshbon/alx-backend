#!/usr/bin/env python3
""" The module for MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ Initialize the MRU Cache"""
        super().__init__()
        self.key_tracker = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data.
            Discard the most recently used item (MRU algorithm).
            Does nothing if key or item is None"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_tracker:
                self.key_tracker.remove(key)
            self.key_tracker.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.key_tracker[-2]
                print("DISCARD:", mru_key)
                self.cache_data.pop(mru_key)
                self.key_tracker.remove(mru_key)

    def get(self, key):
        """ Returns the value in self.cache_data linked to key.
            If key is None or if key doesn't exist in self.cache_data,
            return None."""
        if key is not None and key in self.cache_data:
            if key in self.key_tracker:
                self.key_tracker.remove(key)
            self.key_tracker.append(key)
            return self.cache_data[key]
        return None
