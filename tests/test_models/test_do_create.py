#!/usr/bin/python3
""" """

import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        """ """
        self.cli = HBNBCommand()

    def tearDown(self):
        """ """
        storage.delete_all()

    def test_create_base_model(self):
        """ """
        self.cli.onecmd('create BaseModel name="test" age=18')
        obj_id = self.cli.stdout.split('\n')[0]
        obj = storage.all()['BaseModel.{}'.format(obj_id)]
        self.assertEqual(obj.name, 'test')
        self.assertEqual(obj.age, 18)

    def test_create_base_model_invalid_params(self):
        """ """
        self.cli.onecmd('create BaseModel name="test" age="eighteen" foo=bar')
        obj_id = self.cli.stdout.split('\n')[0]
        obj = storage.all().get('BaseModel.{}'.format(obj_id))
        self.assertIsNone(obj)

    def test_create_invalid_class(self):
        """ """
        self.cli.onecmd('create SomeInvalidClass name="test" age=18')
        output = self.cli.stdout.strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_missing_class(self):
        """ """
        self.cli.onecmd('create')
        output = self.cli.stdout.strip()
        self.assertEqual(output, "** class name missing **")

    def test_create_string_with_underscore(self):
        """ """
        self.cli.onecmd('create BaseModel name="My_little_house"')
        obj_id = self.cli.stdout.split('\n')[0]
        obj = storage.all()['BaseModel.{}'.format(obj_id)]
        self.assertEqual(obj.name, 'My little house')

    def test_create_float_value(self):
        """ """
        self.cli.onecmd('create BaseModel score=3.14')
        obj_id = self.cli.stdout.split('\n')[0]
        obj = storage.all()['BaseModel.{}'.format(obj_id)]
        self.assertEqual(obj.score, 3.14)

    def test_create_integer_value(self):
        """ """
        self.cli.onecmd('create BaseModel age=25')
        obj_id = self.cli.stdout.split('\n')[0]
        obj = storage.all()['BaseModel.{}'.format(obj_id)]
        self.assertEqual(obj.age, 25)
