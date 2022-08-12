"""
File with custom exceptions
"""


class ParserError(Exception):
    def __str__(self):
        return 'Avito.ru parser error'


class AvitoQueryError(Exception):
    def __str__(self):
        return 'Invalid value in the \'query\' or \'region\' field (for avito.ru)'


class DatabaseError(Exception):
    def __str__(self):
        return 'Error in working with the database'
