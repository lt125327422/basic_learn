import string
from pdf.lox.tokenlox import TokenLox
from pdf.lox.tokenType import TokenType



class Scanner:
    start = 0
    current = 0
    line = 0

    Lox = None

    tokens: [TokenLox] = []

    keywords = {
        "and": TokenType.AND,

        "or": TokenType.AND,
        "not": TokenType.AND,
        "super": TokenType.AND,
        "class": TokenType.AND,
        "else": TokenType.AND,

        "false": TokenType.AND,
        "true": TokenType.AND,
        "nil": TokenType.AND,
        "if": TokenType.AND,
        "for": TokenType.AND,

        "while": TokenType.AND,
        "return": TokenType.AND,
        "var": TokenType.AND,
        "print": TokenType.AND,
        "fun": TokenType.AND,

    }

    def __init__(self, source_string: string):
        self.source_code = source_string
        from pdf.lox.Lox import Lox
        self.Lox = Lox
        self.strategy = {
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

            "!": lambda: self.add_token(TokenType.BANG_EQUAL) if self.match('=') else self.add_token(TokenType.BANG),
            "=": lambda: self.add_token(TokenType.EQUAL_EQUAL) if self.match('=') else self.add_token(TokenType.EQUAL),
            "<": lambda: self.add_token(TokenType.GREATER_EQUAL) if self.match('=') else self.add_token(TokenType.LESS),
            ">": lambda: self.add_token(TokenType.LESS_EQUAL) if self.match('=') else self.add_token(TokenType.GREATER),

            "/": self.handle_comment,

            " ": self.loop,
            "\r": self.loop,
            "\t": self.loop,

            "\n": self.line_feed,

            '"': self.string_handle

        }

        return

    def is_at_end(self) -> bool:
        return self.current >= len(self.source_code)

    def advance(self):
        self.current += 1
        return self.source_code[self.current - 1]

    def add_token(self, token_type: TokenType):
        self._add_token(token_type, None)

    def _add_token(self, token_type: TokenType, literal: any):
        self.tokens.append(TokenLox(token_type,
                                    self.source_code[self.start:self.current]
                                    , literal, self.line))

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        return self.tokens

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source_code[self.current]

    def is_digit(self, char):
        # reg = r'[a-zA-Z_][a-zA-Z0-9_]*'
        return char >= '0' and char <= '9'

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()
        self._add_token(TokenType.NUMBER,
                        float(self.source_code[self.start:self.current]))

    def scan_token(self) -> None:
        c: string = self.advance()
        self.strategy.get(c, lambda: self.def_handler(c))()

    def def_handler(self, c):
        if self.is_digit(c):
            self.number()

        elif self.is_alpha(c):
            self.identifier()
        else:
            self.Lox.error(self.line, "Unexpected character.")

    # it's like condition advance()
    def match(self, expect_char):
        if self.is_at_end():
            return False
        if self.source_code[self.current] != expect_char:
            return False
        self.current += 1
        return True

    def peek_next(self):
        if self.current + 1 >= len(self.source_code):
            return '\0'
        return self.source_code[self.current + 1]

    def is_alpha(self, c):
        # re_numbers_str = re.compile(r'\d+')
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

    def is_alpha_numeric(self, c):
        return self.is_alpha(c) or self.is_digit(c)

    def identifier(self):

        #  maximal munch
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        type = self.keywords.get(self.source_code[self.start:self.current],
                                 TokenType.IDENTIFIER)

        self.add_token(type)
        # if type == None :
        #     type = TokenType.IDENTIFIER

    def handle_comment(self):
        if self.match('/'):
            while self.peek() != '\n' and not self.is_at_end():
                self.advance()
        else:
            self.add_token(TokenType.SLASH)

    def loop(self):
        return

    def line_feed(self):
        self.line += 1

    def string_handle(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.is_at_end():
            self.Lox.error(self.line, "Unterminated string.")
            return

        self.advance()

        self._add_token(TokenType.STRING,
                        self.source_code[self.start + 1:self.current - 1])
