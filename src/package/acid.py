from sly import Parser
from lexer import lex
vars = {}
file = open("to.acid").read()
outputs = open("out.acid", "w")
class parser(Parser):
    debugfile = 'parser.out'
    # Get the token list from the lexer (required)
    tokens = lex.tokens

    # Grammar rules and actions
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('ID ASSIGN term')
    def expr(self, p):
        vars[str(p.ID)] = [p.term]

    @_('ID ASSIGN ID')
    def expr(self, p):
        vars[str(p.ID0)] = [p.ID1]

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr
    
    @_('TYPE LPAREN QUOTE ID QUOTE RPAREN')
    def expr(self, p):
        return(p.ID)
    @_('TYPE LPAREN ID RPAREN')
    def expr(self, p):
        if p.ID in vars:
            return(str(vars.get(p.ID)))
        else:
            return("'" + p.ID + "' is not defined at line " + str(p.lineno))
    @_('TYPE LPAREN NUMBER RPAREN')
    def expr(self, p):
        return(p.NUMBER)
    @_('ID JOIN ID')
    def expr(self, p):
        if p.ID0 and p.ID1 in vars:
            return(str(vars.get(p.ID0)) + str(vars.get(p.ID1)))
        elif p.ID1 in vars:
            return(p.ID0 + str(vars.get(p.ID1)))
        elif p.ID0 in vars:
            return(str(vars.get(p.ID0)) + p.ID1)
        else:
            return(p.ID0 + p.ID1)
class acid():
    def run():

        lexer = lex()
        parser = parser()
        line = file.split('\n')
        for l in line:
            the = lexer.tokenize(l)
            parsed = parser.parse(the)
            if parsed == None:
                pass
            else:
                print(parsed)
