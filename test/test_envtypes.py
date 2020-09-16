import unittest
from envtypes import EnvTypes
from dotenv import load_dotenv

load_dotenv()


class CustomArguments(unittest.TestCase):
    def setUp(self):
        self.custom = EnvTypes(use_prefix=False,
                               prefix='dJanGo',
                               value_del='___',
                               env_str='sTr',
                               env_int='INt',
                               env_bool='BOOl',
                               env_list='LiSt',
                               list_value_del=',,',
                               list_type_del=',_,',
                               env_tuple='TuPle',
                               tuple_value_del=',.,',
                               tuple_type_del=',-,',
                               env_dict='DicT',
                               dict_key_del='::',
                               dict_value_del=':=:',
                               dict_type_del=';;',
                               empty_value='naDa',
                               none_value='nONE')

    def test_custom_arguments(self):
        self.values = [False, 'dJanGo', '___', 'sTr', 'INt', 'BOOl',
                       'LiSt', ',,', ',_,', 'TuPle', ',.,', ',-,',
                       'DicT', '::', ':=:', ';;', 'naDa', 'nONE']
        for index in self.values:
            self.assertEqual(
                self.custom.arguments[self.values.index(index)]['value'], index)


class DefaultArguments(unittest.TestCase):
    def setUp(self):
        self.default = EnvTypes()

    def test_default_arguments(self):
        self.values = [True, 'PYTHON_', ';__', 'str', 'int', 'bool',
                       'list', ' - ', ', ', 'tuple', ' - ', ', ',
                       'dict', ':', ' - ', ', ', 'empty', 'none']
        for index in self.values:
            self.assertEqual(
                self.default.arguments[self.values.index(index)]['default_value'], index)
