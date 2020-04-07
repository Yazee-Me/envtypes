from unittest import TestCase
from envtypes.types import EnvTypes
from dotenv import load_dotenv

load_dotenv()


class ConfigTypes(TestCase):
    def setUp(self):
        self.custom = EnvTypes(field_del='---',
                               value_del='___',
                               prefix='pyTHON',
                               env_str='sTr',
                               env_int='INt',
                               env_bool='BOOl',
                               env_lists='LiSt',
                               list_del=',,',
                               env_tuples='TuPle',
                               tuple_del=',.,',
                               env_dict='DicT',
                               dict_del=':=:',
                               empty_value='naDa',
                               none_value='nONE')
        self.config = EnvTypes()

    def test_instance(self):
        self.assertIsInstance(self.custom, EnvTypes)
        self.assertIsInstance(self.config, EnvTypes)

    def test_custom(self):
        self.assertEqual(self.custom.field_del, '---')
        self.assertEqual(self.custom.value_del, '___')
        self.assertEqual(self.custom.prefix, 'PYTHON---')
        self.assertEqual(self.custom.env_str, 'str')
        self.assertEqual(self.custom.env_int, 'int')
        self.assertEqual(self.custom.env_bool, 'bool')
        self.assertEqual(self.custom.env_list, 'list')
        self.assertEqual(self.custom.list_del, ',,')
        self.assertEqual(self.custom.env_tuple, 'tuple')
        self.assertEqual(self.custom.tuple_del, ',.,')
        self.assertEqual(self.custom.env_dict, 'dict')
        self.assertEqual(self.custom.dict_del, ':=:')
        self.assertEqual(self.custom.empty_value, 'naDa')
        self.assertEqual(self.custom.none_value, 'nONE')

    def test_config(self):
        self.assertEqual(self.config.field_del, '_')
        self.assertEqual(self.config.value_del, '; _')
        self.assertEqual(self.config.prefix, 'DJANGO_')
        self.assertEqual(self.config.env_str, 'str')
        self.assertEqual(self.config.env_int, 'int')
        self.assertEqual(self.config.env_bool, 'bool')
        self.assertEqual(self.config.env_list, 'list')
        self.assertEqual(self.config.list_del, ', ')
        self.assertEqual(self.config.env_tuple, 'tuple')
        self.assertEqual(self.config.tuple_del, ', ')
        self.assertEqual(self.config.env_dict, 'dict')
        self.assertEqual(self.config.dict_del, ': ')
        self.assertEqual(self.config.empty_value, 'empty')
        self.assertEqual(self.config.none_value, 'none')

    def test_env_types(self):
        self.assertEqual(self.config.set_env('test_Env_type_stR'), 'test')
        self.assertEqual(self.config.set_env('test_Env_type_inT'), 178)
        self.assertFalse(self.config.set_env('test_Env_TYPE_booL'), False)
        self.assertTrue(self.config.set_env('test_Env_type_BooL_t'), True)
        self.assertEqual(self.config.set_env(
            'test_Env_type_LIST'), [1, 'two'])
        self.assertEqual(self.config.set_env(
            'test_Env_type_tuPLE'), ('three', 4))
        self.assertEqual(self.config.set_env(
            'test_Env_type_DicT'), {'key': 'value'})

    def test_empty_none(self):
        pass

    def test_errors(self):
        #     self.assertEqual(self.config.set_env(
        #         'test_value_del'), 'Delimiter "; _" was not found in field "DJANGO_TEST_VALUE_DEL".')
        #     self.assertEqual(self.config.set_env(
        #         'inferior'), 'The field "DJANGO_INFERIOR" was not found in .env file.')
        #     self.assertEqual(self.config.set_env('test_env_type'),
        #                      'The "strr" was not defined as a type. Error was found in field "DJANGO_TEST_ENV_TYPE')
        pass

    def test_bulk_envs(self):
        self.assertListEqual(self.config.bulk_envs('tEST_app', 5),
                             ['1', '2', '3', '4', '5'])
