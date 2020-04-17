import os
import re


class EnvTypes():
    """Can configure the use or not of the prefix for environment fields,
       the prefix value for fields, delimitation between value and type,
       delimitation between list and tuple values, delimitation between
       dictionary key and value, name used for different environment types:
       strings, integers, booleans, lists, tuples and dictionaries.
       """

    def __init__(self, **kwargs):
        # Field Delimitation
        if kwargs.get('field_del') is None:
            self.field_del = '_'
        else:
            if isinstance(kwargs.get('field_del'), str):
                self.field_del = kwargs.get('field_del')
            else:
                raise ValueError('"field_del" must be a string.')

        # Use prefix
        if kwargs.get('use_prefix') is None:
            self.use_prefix = True
        else:
            if isinstance(kwargs.get('use_prefix'), bool):
                self.use_prefix = kwargs.get('use_prefix')
            else:
                raise ValueError('"use_prefix" must be a boolean.')

        # Prefix
        if self.use_prefix:
            if kwargs.get('prefix') is None:
                self.prefix = 'PYTHON' + self.field_del
            else:
                if isinstance(kwargs.get('prefix'), str):
                    self.prefix = kwargs.get('prefix').upper() + self.field_del
                else:
                    raise ValueError('"prefix" must be a string.')
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
            if isinstance(kwargs.get('env_str'), str):
                self.env_str = kwargs.get('env_str').lower()
            else:
                raise ValueError('"env_str" must be a string.')

        # Integers
        if kwargs.get('env_int') is None:
            self.env_int = 'int'
        else:
            if isinstance(kwargs.get('env_int'), str):
                self.env_int = kwargs.get('env_int').lower()
            else:
                raise ValueError('"env_int" must be a string')

        # Booleans
        if kwargs.get('env_bool') is None:
            self.env_bool = 'bool'
        else:
            if isinstance(kwargs.get('env_bool'), str):
                self.env_bool = kwargs.get('env_bool').lower()
            else:
                raise ValueError('"env_bool" must be a string')

        # Lists
        if kwargs.get('env_list') is None:
            self.env_list = 'list'
        else:
            if isinstance(kwargs.get('env_list'), str):
                self.env_list = kwargs.get('env_list').lower()
            else:
                raise ValueError('"env_list" must be a string')

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
            if isinstance(kwargs.get('env_tuple'), str):
                self.env_tuple = kwargs.get('env_tuple').lower()
            else:
                raise ValueError('"env_tuple" must be a string')

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
            if isinstance(kwargs.get('env_dict'), str):
                self.env_dict = kwargs.get('env_dict').lower()
            else:
                raise ValueError('"env_dict" must be a string')

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
            if isinstance(kwargs.get('empty_value'), str):
                self.empty_value = kwargs.get('empty_value')
            else:
                raise ValueError('"empty_value" must be a string')

        # None Value
        if kwargs.get('none_value') is None:
            self.none_value = 'none'
        else:
            if isinstance(kwargs.get('none_value'), str):
                self.none_value = kwargs.get('none_value')
            else:
                raise ValueError('"none_value" must be a string')

    def check_alpha(self, field_name):
        if isinstance(field_name, str):
            return True
        return False

    def check_type_delimiter(self, c_del):
        self.c_del = c_del
        if isinstance(self.c_del, str):
            self.c_delimiters = [self.list_type_del,
                                 self.tuple_type_del,
                                 self.dict_type_del]
            for item in self.c_delimiters:
                if self.c_del == item:
                    return True
                    break
            raise ValueError(
                f'"{self.c_del}" is not a valid delimiter.')
        else:
            raise ValueError(f'"{self.c_del}" must be a string.')

    def check_type(self, c_type):
        self.c_type = c_type
        if isinstance(self.c_type, str):
            self.c_types = [self.env_str,
                            self.env_int,
                            self.env_bool,
                            self.env_list,
                            self.env_tuple,
                            self.env_dict]
            for item in self.c_types:
                if self.c_type == item:
                    return True
                    break
            raise ValueError(
                f'"{self.c_type}" is not a valid environment type.')
        else:
            raise ValueError(f'"{self.c_type}" must be a string.')

    def split_type(self, s_type, type_del):
        self.s_type = s_type
        self.s_return_type = []
        if self.check_type_delimiter(type_del):
            self.s_type_del = type_del
            if self.s_type.__contains__(self.s_type_del):
                self.s_type = self.s_type.split(self.s_type_del)[0]
                self.s_subtype = self.s_type.split(self.s_type_del)[1]
                if self.check_type(self.s_type):
                    self.s_return_type.append(self.s_type)
                else:
                    return self.check_type(self.s_type)
                if self.check_type(self.e_subtype):
                    self.s_return_type.append(self.e_subtype)
                else:
                    return self.check_type(self.e_subtype)
                return self.s_return_type
            else:
                return self.s_type
        else:
            return self.check_type_delimiter(type_del)

    def extract_type(self, e_type):
        if self.check_type(e_type):
            self.e_type = e_type
            if self.e_type == self.env_list:
                return self.split_type(self.e_type, self.list_type_del)
            elif self.e_type == self.env_tuple:
                return self.split_type(self.e_type, self.tuple_type_del)
            elif self.e_type == self.env_dict:
                return self.split_type(self.e_type, self.dict_type_del)
            else:
                return self.e_type
        else:
            return self.check_type(self.e_type)

    def check_value(self, c_value, c_value_type):
        self.c_value = c_value
        self.c_value_type = self.extract_type(c_value_type)
        if isinstance(self.c_value_type, str):
            if self.c_value_type == self.env_str:
                if isinstance(self.c_value, str):
                    # verify with regex
                    pass
                else:
                    # return error
                    pass
            else:
                pass
        else:
            pass
        if isinstance(self.c_value_type, list):
            pass

    def extract_value(self, e_value):
        if self.check_value(e_value):
            self.e_value = e_value
            if self.env_type == self.env_str:
                if self.e_value == self.none_value:
                    return None
                elif self.e_value == self.empty_value:
                    return ''
                return str(self.e_value)
            elif self.env_type == self.env_int:
                return int(self.e_value)
            elif self.env_type == self.env_bool:
                if self.e_value == 'True':
                    return True
                return False
            elif self.env_type == self.env_list:
                if self.e_value.__contains__(self.list_del):
                    return list(self.e_value.split(self.list_del))
                else:
                    if self.e_value == self.empty_value:
                        return []
                    return [self.e_value]
            elif self.env_type == self.env_tuple:
                if self.e_value.__contains__(self.tuple_del):
                    return tuple(self.e_value.split(self.tuple_del))
                else:
                    if self.e_value == self.empty_value:
                        return tuple()
                    return tuple(self.e_value)
            elif self.env_type == self.env_dict:
                if self.e_value == self.empty_value:
                    return {}
                self.key = self.e_value.split(self.dict_del)[0]
                self.e_value = self.e_value.split(self.dict_del)[1]
                return {self.key: self.e_value}
            else:
                raise ValueError(
                    f'The "{self.env_type}" was not defined as a type. Error was found in field "{self.field}".')
        else:
            return self.check_value(e_value)

    def set_env(self, field_name):
        if self.check_field_name(field_name):
            self.field_name = str(field_name.upper())
            if self.prefix is not None:
                self.field = self.prefix + self.field_name
            else:
                self.field = self.field_name
            self.field_value = os.getenv(self.field)
            if self.field_value is not None:
                if self.field_value.find(self.value_del) is not -1:
                    self.env_value = os.getenv(
                        self.field).split(self.value_del)[0]
                    self.env_type = os.getenv(self.field).split(
                        self.value_del)[1].lower()
                    return self.extract_value(e_value=self.env_value)
                else:
                    raise ValueError(
                        f'The delimiter "{self.value_del}" was not found in "{self.field}".')
            else:
                raise ValueError(
                    f'The field "{self.field}" was not found in .env file.')
        else:
            raise ValueError(f'Field name "{field_name}" must be a string.')

    def bulk_envs(self, field_name, envs, **kwargs):
        if kwargs.get('return_type') is None:
            self.return_type = 'list'
        else:
            self.return_type = kwargs.get('return_type').lower()
        if isinstance(self.return_type, str) and self.return_type == 'list' or self.return_type == 'tuple':
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
