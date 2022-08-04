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

    #   double symbol
    BANG_EQUAL = 11
    EQUAL_EQUAL = 12
    LESS_EQUAL = 13
    GREATER_EQUAL = 14

    BANG = 14
    EQUAL = 14
    GREATER = 14
    LESS = 14
