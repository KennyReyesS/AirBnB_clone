#!/usr/bin/python3
"""
test_file_storage module
"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ tests for file_storage.py """
