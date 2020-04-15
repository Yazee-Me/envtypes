import os
import re


class EnvTypes():
    """Can configure the prefix of environment,
        delimitation between env value and env type, name used
        for different env types: strings, integers, booleans,
        lists, tuples and dictionaries.
        """

    def __init__(self, **kwargs):
        # Field Delimitation
        if kwargs.get('field_del') is None:
            self.field_del = '_'
        else:
            self.field_del = kwargs.get('field_del')

        # Use prefix
        if kwargs.get('use_prefix') is None:
            self.use_prefix = True
        else:
            self.use_prefix = kwargs.get('use_prefix')

        # Prefix
        if self.use_prefix:
            if kwargs.get('prefix') is None:
                self.prefix = 'PYTHON' + self.field_del
            else:
                self.prefix = kwargs.get('prefix').upper() + self.field_del
        else:
            self.prefix = None

        # Value Delimitation
        if kwargs.get('value_del') is None:
            self.value_del = '; _'
        else:
            self.value_del = kwargs.get('value_del')

        # Strings
        if kwargs.get('env_str') is None:
            self.env_str = 'str'
        else:
            self.env_str = kwargs.get('env_str').lower()

        # Integers
        if kwargs.get('env_int') is None:
            self.env_int = 'int'
        else:
            self.env_int = kwargs.get('env_int').lower()

        # Booleans
        if kwargs.get('env_bool') is None:
            self.env_bool = 'bool'
        else:
            self.env_bool = kwargs.get('env_bool').lower()

        # Lists
        if kwargs.get('env_list') is None:
            self.env_list = 'list'
        else:
            self.env_list = kwargs.get('env_list').lower()

        # List value delimitation
        if kwargs.get('list_value_del') is None:
            self.list_value_del = ', '
        else:
            self.list_value_del = kwargs.get('list_value_del')

        # List type delimitation
        if kwargs.get('list_type_del') is None:
            self.list_type_del = ', '
        else:
            self.list_type_del = kwargs.get('list_type_del')

        # # Tuples
        if kwargs.get('env_tuple') is None:
            self.env_tuple = 'tuple'
        else:
            self.env_tuple = kwargs.get('env_tuple').lower()

        # Tuple value delimitation
        if kwargs.get('tuple_value_del') is None:
            self.tuple_value_del = ', '
        else:
            self.tuple_value_del = kwargs.get('tuple_value_del')

        # Tuple type delimitation
        if kwargs.get('tuple_type_del') is None:
            self.tuple_type_del = ', '
        else:
            self.tuple_type_del = kwargs.get('tuple_type_del')

        # # Dictionaries
        if kwargs.get('env_dict') is None:
            self.env_dict = 'dict'
        else:
            self.env_dict = kwargs.get('env_dict').lower()

        # Dictionary key-value delimitation
        if kwargs.get('dict_kv_del') is None:
            self.dict_kv_del = ': '
        else:
            self.dict_kv_del = kwargs.get('dict_kv_del')

        # Dictionary type delimitation
        if kwargs.get('dict_type_del') is None:
            self.dict_type_del = ', '
        else:
            self.dict_type_del = kwargs.get('dict_type_del')

        # Empty Value
        if kwargs.get('empty_value') is None:
            self.empty_value = 'empty'
        else:
            self.empty_value = kwargs.get('empty_value')

        # None Value
        if kwargs.get('none_value') is None:
            self.none_value = 'none'
        else:
            self.none_value = kwargs.get('none_value')

    def check_field_name(self, field_name):
        pass

    def extract_value(self):
        # prefix
        # field delimiter
        # value delimiter
        # field name
        # str
        # int
        # bool
        # list
        # list delimiter
        # tuple
        # tuple delimiter
        # dict
        # dict delimiter
        # env type
        # empty
        # none
        if self.env_type == self.env_str:
            if self.value == self.none_value:
                return None
            elif self.value == self.empty_value:
                return ''
            return str(self.value)
        elif self.env_type == self.env_int:
            return int(self.value)
        elif self.env_type == self.env_bool:
            if self.value == 'True':
                return True
            return False
        elif self.env_type == self.env_list:
            if self.value.__contains__(self.list_del):
                return list(self.value.split(self.list_del))
            else:
                if self.value == self.empty_value:
                    return []
                return [self.value]
        elif self.env_type == self.env_tuple:
            if self.value.__contains__(self.tuple_del):
                return tuple(self.value.split(self.tuple_del))
            else:
                if self.value == self.empty_value:
                    return tuple()
                return tuple(self.value)
        elif self.env_type == self.env_dict:
            if self.value == self.empty_value:
                return {}
            self.key = self.value.split(self.dict_del)[0]
            self.value = self.value.split(self.dict_del)[1]
            return {self.key: self.value}
        else:
            raise NameError(
                f'The "{self.env_type}" was not defined as a type. Error was found in field "{self.field}".')

    def set_env(self, field_name):
        if isinstance(field_name, str):
            self.field_name = str(field_name.upper())
            if self.prefix is not None:
                self.field = self.prefix + self.field_name
            else:
                self.field = self.field_name
            self.field_value = os.getenv(self.field)
            if self.field_value is not None:
                if self.field_value.find(self.value_del) is not -1:
                    self.value = os.getenv(self.field).split(self.value_del)[0]
                    self.env_type = os.getenv(self.field).split(
                        self.value_del)[1].lower()
                    return self.extract_value()
                else:
                    raise NameError(
                        f'The delimiter "{self.value_del}" was not found in "{self.field}".')
            else:
                raise NameError(
                    f'The field "{self.field}" was not found in .env file.')
        else:
            raise ValueError(f'Field name "{field_name}" must be a string.')

    def bulk_envs(self, field_name, return_type, envs):
        if isinstance(return_type, str) and return_type.lower() == 'list' or return_type.lower() == 'tuple':
            self.return_type = return_type.lower()
            if self.return_type == 'list':
                self.env_value_list = []
            elif self.return_type == 'tuple':
                self.env_value_tuple = ()
        else:
            raise ValueError(
                'The "return_type" parameter bust be a string. The only two values accepted are "list" and "tuple" (case insensitive).')

        if isinstance(envs, int) and envs > 1:
            for self.env in range(1, envs+1):
                self.item = self.set_env(f'{field_name}_{self.env}')
                if self.return_type == 'list':
                    self.env_value_list.append(self.item)
                elif self.return_type == 'tuple':
                    self.env_value_tuple += tuple(self.item)
            return self.env_value_list
        else:
            raise ValueError(
                'The "envs" parameter must be an integer type and his value must be bigger than 0 (zero).')
