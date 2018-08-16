#!/usr/bin/python
__author__ = 'agoss'

import unittest

from flatten_json_data import flatten


class UnitTests(unittest.TestCase):
    def test_no_flatten(self):
        dic = {'a': '1', 'b': '2', 'c': 3}
        expected = dic
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_one_flatten(self):
        dic = {'a': '1',
               'b': '2',
               'c': {'c1': '3', 'c2': '4'}
               }
        expected = {'a': '1', 'b': '2', 'c.c1': '3', 'c.c2': '4'}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_one_flatten_utf8(self):
        dic = {'a': '1',
               u'ñ': u'áéö',
               'c': {u'c1': '3', 'c2': '4'}
               }
        expected = {'a': '1', u'ñ': u'áéö', 'c.c1': '3', 'c.c2': '4'}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_one_flatten_utf8_dif(self):
        a = {u'eñe': 1}
        info = dict(info=a)
        expected = {u'info.{}'.format(u'eñe'): 1}
        actual = flatten(info)
        self.assertEqual(actual, expected)

    def test_list(self):
        dic = {
            'a': 1,
            'b': [{'c': [2, 3]}]
        }
        expected = {'a': 1, 'b.0.c.0': 2, 'b.0.c.1': 3}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_list_and_dict(self):
        dic = {
            'a': 1,
            'b': 2,
            'c': [{'d': [2, 3, 4], 'e': [{'f': 1, 'g': 2}]}]
        }
        expected = {'a': 1, 'b': 2, 'c.0.d.0': 2, 'c.0.d.1': 3, 'c.0.d.2': 4,
                    'c.0.e.0.f': 1, 'c.0.e.0.g': 2}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_empty_list_and_dict(self):
        dic = {
            'a': {},
            'b': [],
            'c': '',
            'd': None,
            'e': [{'f': [], 'g': [{'h': {}, 'i': [], 'j': '', 'k': None}]}]
        }
        expected = {'a': {}, 'b': [], 'c': '', 'd': None,
                    'e.0.f': [], 'e.0.g.0.h': {}, 'e.0.g.0.i': [],
                    'e.0.g.0.j': '', 'e.0.g.0.k': None}
        actual = flatten(dic)
        self.assertEqual(actual, expected)

    def test_woodchuck_example(self):
        dic = {
            "id": "0001",
            "type": "woodchuck",
            "name": "Chucky Wood",
            "ppu": 0.55,
            "hairs":
                {
                    "hair":
                        [
                            {"id": "1001", "type": "Yellow-Brown"},
                            {"id": "1002", "type": "Brown-Yellow"},
                            {"id": "1003", "type": "Brown"},
                            {"id": "1004", "type": "Dark Brown"}
                        ]
                },
            "whiskers":
                [
                    {"id": "5001", "type": "Straight"},
                    {"id": "5002", "type": "Crooked"},
                    {"id": "5005", "type": "Thick"},
                    {"id": "5007", "type": "Thin"},
                    {"id": "5006", "type": "Dark"},
                    {"id": "5003", "type": "Light"}
                ]
        }
        expected = {'id': '0001', 'type': 'woodchuck', 'name': 'Chucky Wood', 'ppu': 0.55, 'hairs.hair.0.id': '1001',
                    'hairs.hair.0.type': 'Yellow-Brown', 'hairs.hair.1.id': '1002', 'hairs.hair.1.type': 'Brown-Yellow',
                    'hairs.hair.2.id': '1003', 'hairs.hair.2.type': 'Brown', 'hairs.hair.3.id': '1004',
                    'hairs.hair.3.type': 'Dark Brown', 'whiskers.0.id': '5001', 'whiskers.0.type': 'Straight',
                    'whiskers.1.id': '5002', 'whiskers.1.type': 'Crooked', 'whiskers.2.id': '5005',
                    'whiskers.2.type': 'Thick', 'whiskers.3.id': '5007', 'whiskers.3.type': 'Thin',
                    'whiskers.4.id': '5006', 'whiskers.4.type': 'Dark', 'whiskers.5.id': '5003',
                    'whiskers.5.type': 'Light'}
        actual = flatten(dic)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
