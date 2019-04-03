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


class PrintNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):
        self.value = self.value.evaluate()
        print(self.value)


class BopNode(Node):
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
        if 'true' == v :
            self.value = True
        else:
            self.value = False

    def evaluate(self):
        return self.value

import ply.lex as lex
import ply.yacc as yacc
import sys
import traceback

# ------------------------------------
# Building Lex
# ------------------------------------

# tokens = (
#     'PRINT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE'
#     'NUMBER', 'REAL', 'TUPLE', 'BOOLEAN', 'STRING', 'LIST'
#     'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MOD', 'CONS'
#     'GREATER', 'LESS', 'EQUAL', 'GREATEROREQUAL', 'LESSOREQUAL', 'NOTEQUAL'
#     'NOT', 'AND', 'OR', 'IN'
# )

tokens = (
    'PRINT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
    'NUMBER', 'BOOLEAN',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MOD', 'CONS',
    'GREATER', 'LESS', 'EQUAL', 'GREATEROREQUAL', 'LESSOREQUAL', 'NOTEQUAL',
    'NOT', 'AND', 'OR', 'IN',
)

#Tokens
t_PRINT = 'print'
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
t_MOD = 'mod'
t_CONS = r'::'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL = r'=='
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_NOTEQUAL = r'<>'
t_NOT = r'not'
t_AND = 'andalso'
t_OR = 'orelse'
t_IN = 'in'

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_BOOLEAN(t):
    r'true|false'
    try:
        t.value = BooleanNode(t.value)
    except Exception:
        print(t.value)
    return t


# Ignored characters
t_ignore = " \t"


def t_error(t):
    print("Syntax error at '%s'" % t.value)


lex.lex()
# yacc.yacc()


fp = open('testInput.txt', 'r')
lines = fp.readlines()
code = ""
for line in lines:
    code += line.strip()

try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
        print(token)
    print(code)
    # ast = yacc.parse(code)
    # ast.execute()
except Exception:
    error = traceback.format_exc()
    print("ERROR")
else:
    error = ""
finally:
    print(error)
