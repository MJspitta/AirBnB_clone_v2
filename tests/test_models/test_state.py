#!/usr/bin/python3
""" test for state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test state class"""

    def __init__(self, *args, **kwargs):
        """ initialization"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
