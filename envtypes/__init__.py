import os
import re


class EnvTypes():
    """Can be configured the use or not of the prefix for environment fields,
       the prefix value for fields, delimitation between value and type,
       delimitation between list and tuple values, delimitation between
       dictionary key and value, name used for different environment types:
       strings, integers, booleans, lists, tuples and dictionaries.
       """

    def __init__(self, **kwargs):
        ''''''
        self.string = {'name': 'string', 'class': str, 'regex': r'\w*',
                       'error': 'Allowed characters: a to z, small or capital and underscore sign "_".'},
        self.symbol = {'name': 'symbol', 'class': str, 'regex': r'[^a-zA-Z0-9]*\S*',
                       'error': 'Allowed characters: all symbols without spaces.'},
        self.integer = {'name': 'integer', 'class': int, 'regex': r'',
                        'error': 'Are allowed only digits.'},
        self.boolean = {'name': 'boolean', 'class': bool, 'regex': r'',
                        'error': 'Are allowed only boolean values: "True" or "False".'},
        self.list = {'name': 'list', 'class': list, 'regex': r'',
                     'error': ''},
        self.tuple = {'name': 'tuple', 'class': tuple, 'regex': r'',
                      'error': ''},
        self.dictionary = {'name': 'dictionary', 'class': dict, 'regex': r'',
                           'error': ''},
        self.arguments = [
            {'name': 'use_prefix', 'default_value': True,
             'type': self.boolean},
            {'name': 'prefix', 'default_value': 'PYTHON_',
             'type': self.string},
            {'name': 'value_del', 'default_value': ';__',
             'type': self.symbol},
            {'name': 'env_str', 'default_value': 'str',
             'type': self.string},
            {'name': 'env_int', 'default_value': 'int',
             'type': self.string},
            {'name': 'env_bool', 'default_value': 'bool',
             'type': self.string},
            {'name': 'env_list', 'default_value': 'list',
             'type': self.string},
            {'name': 'list_value_del', 'default_value': ' - ',
             'type': self.symbol},
            {'name': 'list_type_del', 'default_value': ', ',
             'type': self.symbol},
            {'name': 'env_tuple', 'default_value': 'tuple',
             'type': self.string},
            {'name': 'tuple_value_del', 'default_value': ' - ',
             'type': self.symbol},
            {'name': 'tuple_type_del', 'default_value': ', ',
             'type': self.symbol},
            {'name': 'env_dict', 'default_value': 'dict',
             'type': self.string},
            {'name': 'dict_key_del', 'default_value': ':',
             'type': self.symbol},
            {'name': 'dict_value_del', 'default_value': ' - ',
             'type': self.symbol},
            {'name': 'dict_type_del', 'default_value': ', ',
             'type': self.symbol},
            {'name': 'empty_value', 'default_value': 'empty',
             'type': self.string},
            {'name': 'none_value', 'default_value': 'none',
             'type': self.string},
        ]

        for argument in self.arguments:
            self.user_argument = kwargs.get(argument['name'])
            if self.user_argument is not None:
                if (argument['type'] == self.string and
                    isinstance(self.user_argument, self.string[0]['class']) and
                        re.match(self.string[0]['regex'], self.user_argument)):
                    argument['value'] = self.user_argument
                elif (argument['type'] == self.symbol and
                        isinstance(self.user_argument, self.symbol[0]['class']) and
                        re.match(self.symbol[0]['regex'], self.user_argument)):
                    argument['value'] = self.user_argument
                elif (argument['type'] == self.boolean and
                        isinstance(self.user_argument, self.boolean[0]['class'])):
                    argument['value'] = self.user_argument
                else:
                    raise ValueError(
                        f'The "{argument["name"]}" value must be a "{argument["type"][0]["name"]}". {argument["type"][0]["error"]}')
