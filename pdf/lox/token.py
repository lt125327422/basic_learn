import string
from pdf.lox.tokenType import TokenType


class Token:

    def __init__(self, token_type: TokenType, lexeme: string, literal: any, line: int):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
