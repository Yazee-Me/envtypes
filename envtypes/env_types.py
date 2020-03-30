import os
from dotenv import load_dotenv, parser

load_dotenv()

prefix = 'DJANGO_'


def get_values(field_name, **kwargs):
    '''Automate the getting of values from .env file.'''

    # Verify if user changed default delimitation
    delimitation = kwargs.get('delimitation')
    if not delimitation:
        delimitation = '; _'

    # Verify if user changed default notation for strings
    # and lower strings name
    strings = kwargs.get('text')
    if not strings:
        strings = 'str'
    else:
        strings = strings.lower()

    # Verify if user changed default notation for integers
    # and lower integers name
    integers = kwargs.get('number')
    if not integers:
        integers = 'int'
    else:
        integers = integers.lower()

    # Verify if user changed default notation for booleans
    # and lower booleans name
    booleans = kwargs.get('boolean')
    if not booleans:
        booleans = 'bool'
    else:
        booleans = booleans.lower()

    # Verify if user changed default notation for lists
    # and lower lists name
    lists = kwargs.get('lists')
    if not lists:
        lists = 'list'
    else:
        lists = lists.lower()

    # Verify if user changed default notation for tuples
    # and lower tuples name
    tuples = kwargs.get('tuples')
    if not tuples:
        tuples = 'tuple'
    else:
        tuples = tuples.lower()

    # Verify if user changed default notation for dictionaries
    # and lower dictionaries name
    dictionaries = kwargs.get('dictionaries')
    if not dictionaries:
        dictionaries = 'dict'
    else:
        dictionaries = dictionaries.lower()

    env_field = prefix + field_name
    field = os.getenv(env_field).split(delimitation)[0]
    object_type = os.getenv(env_field).split(delimitation)[1]

    if object_type == strings:
        if field == 'None':
            return None
        elif field == 'Empty':
            return ''
        return field
    elif object_type == integers:
        return int(field)
    elif object_type == booleans:
        if field == 'True':
            return True
        return False
    elif object_type == lists:
        if field.__contains__(','):
            return list(field.split(','))
        else:
            if field == 'Empty':
                return []
            return [field]
    elif object_type == tuples:
        if field.__contains__(','):
            return tuple(field.split(','))
        else:
            if field == 'Empty':
                return tuple()
            return tuple(field)
    elif object_type == dictionaries:
        if field == 'Empty':
            return {}
        key = field.split(': ')[0]
        value = field.split(': ')[1]
        return {key: value}
    else:
        return


# verify integer to be valid
