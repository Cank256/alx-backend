#!/usr/bin/env python3
"""
Hypermedia pagination
"""
from typing import List, Dict, Any
from .1-simple_pagination import Server


class Server(Server):
    """Server class with hypermedia pagination"""
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get hypermedia pagination details."""
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + (
            1 if len(self.dataset()) % page_size != 0 else 0)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
