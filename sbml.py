# David Sill 111486160
# Assigment HW 3 CSE 307

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0


class NumberNode(Node):
    def __init__(self, v):
        if ('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value


class ExecuteStatmentNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):
        self.value = self.value.evaluate()
        print(self.value)


class OpNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()

class BooleanNode(Node):
    def __init__(self, v):
        if 'True' == v:
            self.value = True
        else:
            self.value = False

    def evaluate(self):
        return self.value

class NotBooleanNode(Node):
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        if self.value.evaluate():
            return False
        else:
            return True

class BooleanOpNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == 'andalso'):
            return self.v1.evaluate() and self.v2.evaluate()
        elif (self.op == 'orelse'):
            return self.v1.evaluate() or self.v2.evaluate()

import ply.lex as lex
import ply.yacc as yacc
import sys
import traceback
import string

# ------------------------------------
#           Building Lex
# ------------------------------------

reserved = {
    'print' : 'PRINT',
    'mod' : 'MOD',
    'andalso' : 'AND',
    'orelse' : 'OR',
    'in' : 'IN',
    'not' : 'NOT',
    'True': 'TRUE',
    'False' : 'FALSE'
 }

tokens = [
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'CONS', 'POUND',
    'GREATER', 'LESS', 'EQUAL', 'GREATEROREQUAL', 'LESSOREQUAL', 'NOTEQUAL'
] + list(reserved.values())

#Tokens
t_PRINT = 'print'
t_MOD = 'mod'
t_AND = 'andalso'
t_OR = 'orelse'
t_IN = 'in'
t_NOT = 'not'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_SEMICOLON = r'\;'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\*\*'
t_CONS = r'::'
t_POUND = r'\#'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL = r'=='
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_NOTEQUAL = r'<>'

def t_TRUE(t):
    'True'
    t.value = BooleanNode(t.value)
    return t

def t_FALSE(t):
    'False'
    t.value = BooleanNode(t.value)
    return t

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t\n"


def t_error(t):
    print("Syntax error at '%s'" % t.value)

lex.lex()

# -------------------------------------------
#               Parsing
# -------------------------------------------

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)
def p_statement_exp(t):
    '''statement : expression SEMICOLON
         | boolean SEMICOLON
    '''
    t[0] = ExecuteStatmentNode(t[1])


def p_expression_op(t):
    '''expression : expression PLUS factor
                  | expression MINUS factor
                  | expression TIMES factor
                  | expression DIVIDE factor '''
    t[0] = OpNode(t[2], t[1], t[3])


def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]



def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]

# def p_factor_expression(t):
#     'factor : LPAREN expression RPAREN'
#     t[0] = t[2]
#
def p_boolean_op(t):
    '''
    boolean : boolean AND boolean
        | boolean OR boolean
    '''
    t[0] = BooleanOpNode(t[2], t[1], t[3])

def p_boolean_not(t):
    'boolean : NOT boolean'
    t[0] = NotBooleanNode(t[2])

def p_boolean(t):
    '''
    boolean : TRUE
        | FALSE
    '''
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

yacc.yacc()


file = open('testInput.txt', 'r')
lines = file.readlines()
print(lines)
code = ""
for line in lines:
    # if len(line) < 2: continue
    code = line.strip()
    try:
        lex.input(code)
        while True:
            token = lex.token()
            if not token: break
            print(token)
        print(code)
        ast = yacc.parse(code)
        ast.execute()
    except Exception:
        error = traceback.format_exc()
        print("ERROR")
    else:
        error = ""
    finally:
        print(error)
