from unittest import TestCase
from envtypes.types import EnvTypes
from dotenv import load_dotenv

load_dotenv()


class ConfigTypes(TestCase):
    def setUp(self):
        self.custom = EnvTypes(field_del='---',
                               use_prefix=True,
                               prefix='dJanGo',
                               value_del='___',
                               env_str='sTr',
                               env_int='INt',
                               env_bool='BOOl',
                               env_lists='LiSt',
                               list_value_del=',,',
                               list_type_del=',_,',
                               env_tuples='TuPle',
                               tuple_value_del=',.,',
                               tuple_type_del=',-,',
                               env_dict='DicT',
                               dict_kv_del=':=:',
                               dict_type_del='::',
                               empty_value='naDa',
                               none_value='nONE')
        self.custom_2 = EnvTypes(use_prefix=False,
                                 prefix=None)
        self.config = EnvTypes()

    def test_instance(self):
        self.assertIsInstance(self.custom, EnvTypes)
        self.assertIsInstance(self.config, EnvTypes)

    def test_custom(self):
        self.assertEqual(self.custom.field_del, '---')
        self.assertTrue(self.custom.use_prefix)
        self.assertEqual(self.custom.prefix, 'DJANGO---')
        self.assertEqual(self.custom.value_del, '___')
        self.assertEqual(self.custom.env_str, 'str')
        self.assertEqual(self.custom.env_int, 'int')
        self.assertEqual(self.custom.env_bool, 'bool')
        self.assertEqual(self.custom.env_list, 'list')
        self.assertEqual(self.custom.list_value_del, ',,')
        self.assertEqual(self.custom.list_type_del, ',_,')
        self.assertEqual(self.custom.env_tuple, 'tuple')
        self.assertEqual(self.custom.tuple_value_del, ',.,')
        self.assertEqual(self.custom.tuple_type_del, ',-,')
        self.assertEqual(self.custom.env_dict, 'dict')
        self.assertEqual(self.custom.dict_kv_del, ':=:')
        self.assertEqual(self.custom.dict_type_del, '::')
        self.assertEqual(self.custom.empty_value, 'naDa')
        self.assertEqual(self.custom.none_value, 'nONE')

    def test_custom_2(self):
        self.assertFalse(self.custom_2.use_prefix)
        self.assertEqual(self.custom_2.prefix, None)

    def test_config(self):
        self.assertEqual(self.config.field_del, '_')
        self.assertEqual(self.config.value_del, '; _')
        self.assertTrue(self.config.use_prefix)
        self.assertEqual(self.config.prefix, 'PYTHON_')
        self.assertEqual(self.config.env_str, 'str')
        self.assertEqual(self.config.env_int, 'int')
        self.assertEqual(self.config.env_bool, 'bool')
        self.assertEqual(self.config.env_list, 'list')
        self.assertEqual(self.config.list_value_del, ', ')
        self.assertEqual(self.config.list_type_del, ', ')
        self.assertEqual(self.config.env_tuple, 'tuple')
        self.assertEqual(self.config.tuple_value_del, ', ')
        self.assertEqual(self.config.tuple_type_del, ', ')
        self.assertEqual(self.config.env_dict, 'dict')
        self.assertEqual(self.config.dict_kv_del, ': ')
        self.assertEqual(self.config.dict_type_del, ', ')
        self.assertEqual(self.config.empty_value, 'empty')
        self.assertEqual(self.config.none_value, 'none')

    def test_env_types(self):
        self.assertEqual(self.config.set_env('test_env_type_str'), 'test')
        self.assertEqual(self.config.set_env('test_env_type_int'), 178)
        self.assertFalse(self.config.set_env('test_env_type_bool'))
        self.assertTrue(self.config.set_env('test_env_type_bool_t'))
        # list
        self.assertEqual(self.config.set_env(
            'test_env_type_list_single'), ['single list'])
        self.assertEqual(self.config.set_env('test_env_type_list_str'), [
                         'string one', 'string two'])
        self.assertEqual(self.config.set_env(
            'test_env_type_list_int'), [1, 3, 5, 7])
        self.assertEqual(self.config.set_env(
            'test_env_type_list_bool'), [True, False, False])
        # tuple
        self.assertEqual(self.config.set_env(
            'test_env_type_tuple_single'), ('single tuple'))
        self.assertEqual(self.config.set_env(
            'test_env_type_tuple_str'), ('string three', 'string four'))
        self.assertEqual(self.config.set_env(
            'test_env_type_tuple_int'), (2, 4, 6, 8))
        self.assertEqual(self.config.set_env(
            'test_env_type_tuple_bool'), (False, False, True))
        # dictionary
        self.assertEqual(self.config.set_env(
            'test_env_type_dict_str'), {'string': 'value'})
        self.assertEqual(self.config.set_env(
            'test_env_type_dict_bool'), {'integer': 48})
        self.assertEqual(self.config.set_env(
            'test_env_type_dict_bool'), {'boolean': False})

    def test_bulk_envs(self):
        # list
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_list_str', 3), ['STR 1', 'STR 2', 'STR 3'])
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_list_int', 3), [1, 2, 3])
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_list_bool', 2), [True, False])
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_list_mixed', 3), ['String ONE', 14, False])
        # tuple
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_tuple_str', 3), ('STR 3', 'STR 2', 'STR 1'))
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_tuple_int', 3), (3, 2, 1))
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_tuple_bool', 2), (False, True))
        self.assertEqual(self.config.bulk_envs(
            'test_bulk_tuple_mixed', 3), ('String TWO', 24, False))

    def test_empty_none(self):
        self.assertEqual(self.config.set_env('test_empty_str'), '')
        self.assertEqual(self.config.set_env('test_none_str'), None)
        self.assertEqual(self.config.set_env('test_empty_list'), [])
        self.assertEqual(self.config.set_env('test_empty_tuple'), ())
        self.assertEqual(self.config.set_env('test_empty_dict'), {})

    def test_errors(self):
        pass
