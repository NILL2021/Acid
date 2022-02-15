from multiprocessing.dummy import JoinableQueue
from sly import Lexer

class lex(Lexer):
    # Set of token names.   This is always required
    tokens = { NUMBER, ID, WHILE, IF, ELSE, TYPE,
               PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
               EQ, LT, LE, GT, GE, NE, LPAREN, RPAREN, QUOTE, JOIN}


    literals = { '(', ')', '{', '}', ';' }

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    JOIN = r':'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ      = r'=='
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NE      = r'!='
    LPAREN = r'\('
    RPAREN = r'\)'
    QUOTE = r'\''


    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['type'] = TYPE
    ID['is'] = ASSIGN

    ignore_comment = r'\~.*'
    ignore_space = ' '

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value) 

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1