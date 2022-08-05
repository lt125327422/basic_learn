class TokenLox:

    def __repr__(self):
        return "lexeme = " + self.lexeme + "   token_type"

    def __init__(self, token_type, lexeme, literal, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
