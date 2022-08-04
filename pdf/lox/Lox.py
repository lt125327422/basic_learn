import string


class Lox:
    has_error = False

    @classmethod
    def error(cls, line: int, msg: string):
        Lox.report(line,"",msg)
        return

    @classmethod
    def report(cls, line, where, msg):
        Lox.has_error = True
        print("[line " + line + "] Error" + where + ": " + msg)
