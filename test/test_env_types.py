from unittest import TestCase
from envtypes.env_types import EnvTypes


class ConfigTypesWithKwargs(TestCase):
    def setUp(self):
        self.config = EnvTypes(field_name='stRINGs',
                               field_del='_',
                               value_del='___',
                               prefix='django',
                               env_str='STrings',
                               env_int='inteGERS',
                               env_bool='BOOLeans',
                               env_list='lisTS',
                               list_del='; ',
                               env_tuple='tUPles',
                               tuple_del=' ',
                               env_dict='DICtionaries',
                               dict_del='/',
                               none_value='None',
                               empty_value='emPty')
        self.strings = EnvTypes(field_name='STR')
        self.integers = EnvTypes(field_name='INT')
        self.booleans = EnvTypes(field_name='BOOL')
        self.lists = EnvTypes(field_name='LIST')
        self.tuples = EnvTypes(field_name='TUPLE')
        self.dictionaries = EnvTypes(field_name='DICT')

    # Field Name
    def test_field_name(self):
        self.assertEqual(self.config.field_name, 'STRINGS')

    # Field delimitation
    def test_field_del(self):
        self.assertEqual(self.config.field_del, '_')

    # Value delimitation
    def test_value_del(self):
        self.assertEqual(self.config.value_del, '___')

    # Prefix
    def test_prefix(self):
        self.assertEqual(self.config.prefix, 'DJANGO_')

    # Strings
    def test_env_str(self):
        self.assertEqual(self.config.env_str, 'strings')

    def test_set_env_str(self):
        self.assertEqual(self.strings.set_env(),
                         'A test to see if everything works ok')

    # Integers
    def test_env_int(self):
        self.assertEqual(self.config.env_int, 'integers')

    def test_set_env_int(self):
        self.assertEqual(self.integers.set_env(), 13)

    # Booleans
    def test_env_bool(self):
        self.assertEqual(self.config.env_bool, 'booleans')

    def test_set_env_bool(self):
        self.assertEqual(self.booleans.set_env(), False)

    # Lists
    def test_env_list(self):
        self.assertEqual(self.config.env_list, 'lists')

    def test_list_del(self):
        self.assertEqual(self.config.list_del, '; ')

    def test_set_env_list(self):
        self.assertEqual(self.lists.set_env(), ['first', 'second'])

    # Tuples
    def test_env_tuple(self):
        self.assertEqual(self.config.env_tuple, 'tuples')

    def test_tuple_del(self):
        self.assertEqual(self.config.tuple_del, ' ')

    def test_set_env_tuple(self):
        self.assertEqual(self.tuples.set_env(), ('third', 'fourth'))

    # Dictionaries
    def test_env_dict(self):
        self.assertEqual(self.config.env_dict, 'dictionaries')

    def test_dict_del(self):
        self.assertEqual(self.config.dict_del, '/')

    def test_set_env_dict(self):
        self.assertEqual(self.dictionaries.set_env(), {'key': 'value'})

    # None value
    def test_none_value(self):
        self.assertEqual(self.config.none_value, 'none')

    # Empty value
    def test_empty_value(self):
        self.assertEqual(self.config.empty_value, 'empty')

    # Field
    def test_field(self):
        self.assertEqual(self.config.field, 'DJANGO_STRINGS')

    # Value
    def test_value(self):
        self.assertEqual(self.config.value, 'Something usefull')

    # Object type
    def test_object_type(self):
        self.assertEqual(self.config.object_type, 'strings')
