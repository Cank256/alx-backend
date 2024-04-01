#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict, Any
from .1-simple_pagination import Server


class Server(Server):
    """Server class with deletion-resilient hypermedia pagination"""
    def __init__(self):
        super().__init__()
        self.__indexed_dataset = None

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[
        str, Any
    ]:
        """Get hypermedia pagination details based on index."""
        assert index is None or (isinstance(index, int) and 0 <= index < len(
            self.indexed_dataset())), "Invalid index"
        data = []
        next_index = None
        if index is not None:
            next_index = index + page_size
            for i in range(index, min(index + page_size, len(
                self.indexed_dataset()))
            ):
                if i in self.indexed_dataset():
                    data.append(self.indexed_dataset()[i])
        total_pages = len(self.indexed_dataset()) // page_size + (
            1 if len(self.indexed_dataset()) % page_size != 0 else 0)
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
            "total_pages": total_pages
        }
