from enum import Enum


class TokenType(Enum):
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    COMMA = 5
    DOT = 6
    MINUS = 7
    PLUS = 8
    SEMICOLON = 9
    STAR = 10

    #   double symbol  One or two character tokens.
    BANG_EQUAL = 11
    EQUAL_EQUAL = 12
    LESS_EQUAL = 13
    GREATER_EQUAL = 14
    BANG = 14
    EQUAL = 14
    GREATER = 14
    LESS = 14
    SLASH = 15  # /

    # // Literals.
    IDENTIFIER = 16
    STRING = 17
    NUMBER = 18

    # // Keywords.
    AND = 19
    CLASS = 20
    ELSE = 21
    FALSE = 22
    FUN = 23
    FOR = 24
    IF = 25
    NIL = 26
    OR = 27
    PRINT = 28
    RETURN = 29
    SUPER = 30
    THIS = 31
    TRUE = 32
    VAR = 33
    WHILE = 34

    EOF = 35
