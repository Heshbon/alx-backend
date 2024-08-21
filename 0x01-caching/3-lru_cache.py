#!/usr/bin/env python3
""" The module for LRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ Initialize the LRU Cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assigns item value for the key in self.cache_data dictionary.
            Discards the least recently used item (LRU algorithm).
            Does nothing if key or item is None."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                print("DISCARD:", discarded)
                self.cache_data.pop(discarded)

    def get(self, key):
        """ Returns the value in self.cache_data linked to key.
            Returns None if key is None or key doesn't exist"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
