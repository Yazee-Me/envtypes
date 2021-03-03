from dotenv import load_dotenv
from envtypes import EnvTypes
import unittest

load_dotenv()


class CustomArguments(unittest.TestCase):
    def setUp(self):
        self.custom = EnvTypes(case_sensitive=False,
                               use_prefix=False,
                               prefix='dJanGo',
                               env_del='___',
                               env_str='sTr',
                               env_int='INt',
                               env_bool='BOOl',
                               bool_true_value='True',
                               bool_false_value='False',
                               env_list='LiSt',
                               list_value_del=',,',
                               list_type_del=',_,',
                               env_tuple='TuPle',
                               tuple_value_del=',.,',
                               tuple_type_del=',-,',
                               env_dict='DicT',
                               dict_key_del='::',
                               dict_value_del=':=: ',
                               dict_type_del=';;',
                               empty_value='naDa',
                               none_value='nONE')

    def test_custom_arguments(self):
        self.values = [False, False, 'dJanGo', '___', 'str', 'int', 'bool',
                       'True', 'False', 'list', ',,', ',_,', 'tuple', ',.,',
                       ',-,', 'dict', '::', ':=: ', ';;', 'naDa', 'nONE']
        for index in self.values:
            self.assertEqual(
                self.custom.arguments[self.values.index(index)]['value'],
                index)


class Defaults(unittest.TestCase):
    def setUp(self):
        self.default = EnvTypes()

    def test_default_arguments(self):
        self.values = [True, True, 'PYTHON_', ';__', 'str', 'int', 'bool',
                       'True', 'False', 'list', ' - ', ', ', 'tuple', ' - ',
                       ', ', 'dict', ': ', ' - ', ', ', 'empty', 'none']
        for index in self.values:
            self.assertEqual(
                self.default.arguments[self.values.index(index)]['value'],
                index)

    def test_argument_name(self):
        self.assertTrue(self.default.check_argument_name('test_1'))

    def test_prefix(self):
        self.assertEqual(self.default.check_prefix(
            'something'), 'PYTHON_SOMETHING')

    def test_env_existence(self):
        self.assertTrue(self.default.check_env_existence(
            'test_2', 'something_env_existence'))

    def test_env_del(self):
        self.assertTrue(self.default.check_env_del(
            'test_3', 'something_env_del;__str'))

    def test_list_dels(self):
        self.assertTrue(self.default.check_list_dels(
            'test_4', 'something_list - str, False - bool, 140 - int'))

    def test_tuple_dels(self):
        self.assertTrue(self.default.check_tuple_dels(
            'test_5', 'something_tuple - str, True - bool, 141 - int'))

    def test_dict_dels(self):
        self.assertTrue(self.default.check_dict_dels(
            'test_6', 'dict_key_1: something_dict - str, dict_key_2: True - bool, dict_key_3: 141 - int'))

    def test_env_type(self):
        self.assertTrue(self.default.check_env_type('test_7', 'int'))

    def test_convert_value_str(self):
        self.assertEqual(self.default.convert_value(
            'test_11', 'something_convert_value_str', 'str'),
            'something_convert_value_str')

    def test_convert_value_int(self):
        self.assertEqual(self.default.convert_value(
            'test_12', 143, 'int'), 143)

    def test_convert_value_bool(self):
        self.assertEqual(self.default.convert_value(
            'test_13', 'False', 'bool'), False)

    def test_extract_value_str(self):
        self.assertEqual(self.default.extract_value(
            'test_14', 'some string from environment;__str'),
            'some string from environment')

    def test_extract_value_int(self):
        self.assertEqual(self.default.extract_value(
            'test_15', '234;__int'), 234)

    def test_extract_value_bool(self):
        self.assertEqual(self.default.extract_value(
            'test_16', 'True;__bool'), True)

    def test_extract_value_list(self):
        self.assertEqual(self.default.extract_value(
            'test_17', 'some - str, 123 - int, False - bool;__list'), [
                'some', 123, False])

    def test_extract_value_tuple(self):
        self.assertEqual(self.default.extract_value(
            'test_18', 'some - str, 123 - int, False - bool;__tuple'), (
                'some', 123, False))

    def test_extract_value_dict(self):
        self.assertEqual(self.default.extract_value(
            'test_19', 'key_1: some - str, key_2: 123 - int, key_3: False - bool;__dict'), {
                'key_1': 'some', 'key_2': 123, 'key_3': False})

    def test_extract_value_str_empty(self):
        self.assertEqual(self.default.extract_value(
            'test_20', 'empty;__str'), '')

    def test_extract_value_int_empty(self):
        self.assertEqual(self.default.extract_value(
            'test_21', 'empty;__int'), '')

    def test_extract_value_bool_empty(self):
        self.assertEqual(self.default.extract_value(
            'test_22', 'empty;__bool'), '')

    def test_extract_value_list_empty(self):
        self.assertEqual(self.default.extract_value(
            'test_23', 'empty;__list'), [])

    def test_extract_value_tuple_empty(self):
        self.assertEqual(self.default.extract_value(
            'test_24', 'empty;__tuple'), ())

    def test_extract_value_dict_empty(self):
        self.assertEqual(self.default.extract_value(
            'test_25', 'empty;__dict'), {})

    def test_extract_value_str_none(self):
        self.assertEqual(self.default.extract_value(
            'test_26', 'none;__str'), None)

    def test_extract_value_int_none(self):
        self.assertEqual(self.default.extract_value(
            'test_27', 'none;__int'), None)

    def test_extract_value_bool_none(self):
        self.assertEqual(self.default.extract_value(
            'test_28', 'none;__bool'), None)

    def test_extract_value_list_none(self):
        self.assertEqual(self.default.extract_value(
            'test_29', 'none;__list'), None)

    def test_extract_value_tuple_none(self):
        self.assertEqual(self.default.extract_value(
            'test_30', 'none;__tuple'), None)

    def test_extract_value_str_none(self):
        self.assertEqual(self.default.extract_value(
            'test_31', 'none;__str'), None)

    def test_extract_value_int_none(self):
        self.assertEqual(self.default.extract_value(
            'test_32', 'none;__int'), None)

    def test_extract_value_bool_none(self):
        self.assertEqual(self.default.extract_value(
            'test_33', 'none;__bool'), None)

    def test_extract_value_list_none(self):
        self.assertEqual(self.default.extract_value(
            'test_34', 'none;__list'), None)

    def test_extract_value_tuple_none(self):
        self.assertEqual(self.default.extract_value(
            'test_35', 'none;__tuple'), None)

    def test_extract_value_dict_none(self):
        self.assertEqual(self.default.extract_value(
            'test_36', 'none;__dict'), None)

    def test_set_env_str(self):
        self.assertEqual(self.default.set_env(
            "string"), "some string from environment")

    def test_set_env_int(self):
        self.assertEqual(self.default.set_env(
            "integer"), 123)

    def test_set_env_bool(self):
        self.assertEqual(self.default.set_env(
            "boolean"), False)

    def test_set_env_list(self):
        self.assertEqual(self.default.set_env(
            "list"), ['something_list', 'again', False, 141])

    def test_set_env_tuple(self):
        self.assertEqual(self.default.set_env(
            "tuple"), ('something_tuple', 'again', True, 142))

    def test_set_env_dict(self):
        self.assertEqual(self.default.set_env(
            "dictionary"), {'dict_key_1': 'dict_string_value',
                            'dict_key_2': False, 'dict_key_3': 143})

    def test_set_env_str_empty(self):
        self.assertEqual(self.default.set_env(
            "string_empty"), '')

    def test_set_env_int_empty(self):
        self.assertEqual(self.default.set_env(
            "integer_empty"), '')

    def test_set_env_bool_empty(self):
        self.assertEqual(self.default.set_env(
            "boolean_empty"), '')

    def test_set_env_list_empty(self):
        self.assertEqual(self.default.set_env(
            "list_empty"), [])

    def test_set_env_tuple_empty(self):
        self.assertEqual(self.default.set_env(
            "tuple_empty"), ())

    def test_set_env_dict_empty(self):
        self.assertEqual(self.default.set_env(
            "dictionary_empty"), {})

    def test_set_env_str_none(self):
        self.assertEqual(self.default.set_env(
            "string_none"), None)

    def test_set_env_int_none(self):
        self.assertEqual(self.default.set_env(
            "integer_none"), None)

    def test_set_env_bool_none(self):
        self.assertEqual(self.default.set_env(
            "boolean_none"), None)

    def test_set_env_list_none(self):
        self.assertEqual(self.default.set_env(
            "list_none"), None)

    def test_set_env_tuple_none(self):
        self.assertEqual(self.default.set_env(
            "tuple_none"), None)

    def test_set_env_dict_none(self):
        self.assertEqual(self.default.set_env(
            "dictionary_none"), None)

    def test_set_bulk_envs_list(self):
        self.assertEqual(self.default.set_bulk_envs('envs_list', 'list'), [
                         'string_1', 6, False,
                         ['string_list', 1, True],
                         ('string_tuple', 2, False),
                         {'string': 'string_dict',
                          'integer': 3, 'boolean': False}])

    def test_set_bulk_envs_tuple(self):
        self.assertEqual(self.default.set_bulk_envs('envs_tuple', 'tuple'), (
                         'string_1', 6, False,
                         ['string_list', 1, True],
                         ('string_tuple', 2, False),
                         {'string': 'string_dict',
                          'integer': 3, 'boolean': False}))
