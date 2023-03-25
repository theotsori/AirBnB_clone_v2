#!/usr/bin/python3
""" Test case for do create """

import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsoleCreate(unittest.TestCase):
    """Test console create command"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_create_valid_with_params(self):
        """Test create command with valid class and params"""
        self.console.onecmd("create BaseModel name=\"My House\" value=4.2 flag=True")
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("My House", file_content)
            self.assertIn("4.2", file_content)
            self.assertIn("True", file_content)

    def test_create_valid_with_params_quote(self):
        """Test create command with quotes in params"""
        self.console.onecmd("create BaseModel name=\"My \\\"Big\\\" House\"")
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn('My "Big" House', file_content)

    def test_create_valid_with_params_underscore(self):
        """Test create command with underscores in params"""
        self.console.onecmd("create BaseModel name=\"My_little_house\"")
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("My little house", file_content)

    def test_create_valid_with_params_int(self):
        """Test create command with integer param"""
        self.console.onecmd("create BaseModel value=42")
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("42", file_content)

    def test_create_valid_with_params_float(self):
        """Test create command with float param"""
        self.console.onecmd("create BaseModel value=42.24")
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn("42.24", file_content)

    def test_create_valid_with_params_invalid(self):
        """Test create command with invalid param"""
        self.console.onecmd("create BaseModel value=invalid")
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertNotIn("value", file_content)
