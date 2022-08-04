import string

from pdf.lox.Lox import Lox
from pdf.lox.token import Token
from pdf.lox.tokenType import TokenType


class Scanner:
    start = 0
    current = 0
    line = 0

    tokens = []

    def __init__(self, source_string: string):
        self.source_code = source_string

        return

    def is_at_end(self) -> bool:
        return self.current >= len(self.source_code)

    def advance(self):
        self.current += 1
        return self.source_code[self.current - 1]

    def add_token(self, token_type: TokenType):
        self._add_token(token_type, None)

    def _add_token(self, token_type: TokenType, literal: any):
        self.tokens.append(Token(token_type,
                                 self.source_code[self.start:self.current]
                                 , literal, self.line))

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_tokens()

    def scan_token(self):
        c: string = self.advance()

        strategy = {
            "(": lambda: self.add_token(TokenType.LEFT_PAREN),
            ")": lambda: self.add_token(TokenType.RIGHT_PAREN),
            "{": lambda: self.add_token(TokenType.LEFT_BRACE),
            "}": lambda: self.add_token(TokenType.RIGHT_BRACE),
            ",": lambda: self.add_token(TokenType.COMMA),
            ".": lambda: self.add_token(TokenType.DOT),
            "-": lambda: self.add_token(TokenType.MINUS),
            "+": lambda: self.add_token(TokenType.PLUS),
            ";": lambda: self.add_token(TokenType.SEMICOLON),
            "*": lambda: self.add_token(TokenType.STAR),

            "!": lambda: self.add_token(TokenType.STAR),
            "=": lambda: self.add_token(TokenType.STAR),
            "<": lambda: self.add_token(TokenType.STAR),
            ">": lambda: self.add_token(TokenType.STAR),


        }

        def def_handler():
            Lox.error(self.line, "Unexpected character.")
            return

        strategy.get(c, def_handler)()
        return

    def match(self, expect_char):
        if self.is_at_end():
            return False
        if self.source_code[self.current] != expect_char:
            return False
        self.current += 1
        return True
