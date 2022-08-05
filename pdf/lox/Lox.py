import string
# import pdf.lox.scanner as scanner_space
from pdf.lox.scanner import Scanner


class Lox:
    has_error = False

    @classmethod
    def error(cls, line: int, msg: string):
        cls.report(line, "", msg)
        return

    @classmethod
    def report(cls, line, where, msg):
        cls.has_error = True
        print("[line " + line + "] Error" + where + ": " + msg)

    @classmethod
    def run_file(cls, path):
        with open(path) as file_object:
            source_code = file_object.read()
            cls.run(source_code)

    @classmethod
    def run(cls, source_code):
        scanner = Scanner(source_code)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)


if __name__ == '__main__':
    Lox.run_file('./test/expression/base.lox')
