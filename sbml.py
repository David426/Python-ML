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


class NegateNode(Node):
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        return self.value.evaluate() * -1

class EOPNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def evaluate(self):
        return self.v1.evaluate() * (10 ** self.v2.evaluate())

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
        if self.op == '+':
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == 'div'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op == 'mod'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op == '**'):
            return self.v1.evaluate() ** self.v2.evaluate()

class IsEqualNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op
    def evaluate(self):
        if(self.op == '=='):
            return self.v1.evaluate() == self.v2.evaluate()
        elif(self.op == ',>'):
            return self.v1.evaluate() != self.v2.evaluate()

class ComparisonNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '>'):
            return self.v1.evaluate() > self.v2.evaluate()
        elif (self.op == '<'):
            return self.v1.evaluate() < self.v2.evaluate()
        elif (self.op == '>='):
            return self.v1.evaluate() >= self.v2.evaluate()
        elif (self.op == '<='):
            return self.v1.evaluate() <= self.v2.evaluate()
        elif (self.op == '=='):
            return self.v1.evaluate() == self.v2.evaluate()


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


class StringNode(Node):
    def __init__(self, v):
        if v[0] == '\'' or v[0] == '\"':
            self.v = v[1:len(v)-1]
        else:
            self.v = v

    def output(self):
        return '\'' + self.value + '\''

    def get(self, index):
        return StringNode(self.v[index.evaluate()])

    def evaluate(self):
        return self.v


class ConcatNode(Node):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def evaluate(self):
        return self.s1.evaluate() + self.s2.evaluate()

class ListNode(Node):
    def __init__(self, v):
        if v is not None:
            self.v = [v]
        else:
            self.v = []

    def append(self, elm):
        self.v.append(elm)

    def prepend(self, elm):
        self.v.insert(0, elm)

    def get(self, index):
        return self.v[index.evaluate()]

    def evaluate(self):
        l = []
        for node in self.v:
            l.append(node.evaluate())
        return l


class InList(Node):

    def __init__(self, item, list):
        self.item = item
        self.list = list

    def evaluate(self):
        return self.item.evaluate() in self.list.evaluate()

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
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON',
    'NUMBER', 'EOP', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'DIV', 'POWER', 'CONS', 'POUND',
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
t_COMMA = r','
t_SEMICOLON = r'\;'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DIV = 'div'
t_POWER = r'\*\*'
t_CONS = r'::'
t_POUND = r'\#'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL = r'=='
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_NOTEQUAL = r'<>'
t_EOP = r'e'

def t_STRING(t):
    r'\"([^\"\'])*\"|\'([^\'\"])*\''
    t.value = StringNode(t.value)
    return t

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
    ('left', 'LBRACE', 'RBRACE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'EQUAL', 'NOTEQUAL', 'GREATER', 'GREATEROREQUAL', 'LESS', 'LESSOREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIV'),
    ('right', 'POWER'),
    ('left', 'EOP'),
    ('right', 'UMINUS')
)

def p_statement_exp(t):
    '''statement : expression SEMICOLON
         | boolean SEMICOLON
         | list SEMICOLON
    '''
    t[0] = ExecuteStatmentNode(t[1])

def p_string_exp(t):
    '''statement : STRING SEMICOLON
    '''

    t[0] = ExecuteStatmentNode(t[1])

def p_parenthesis(t):
    '''
    factor : LPAREN expression RPAREN
    '''
    t[0] = t[2]

def p_concat(t):
    '''
    expression : STRING PLUS STRING
        | list PLUS list
    '''
    t[0] = ConcatNode(t[1], t[3])

def p_expression_op(t):
    '''expression : expression PLUS factor
                  | expression MINUS factor
                  | expression TIMES factor
                  | expression DIVIDE factor
                  | expression DIV factor
                  | expression MOD factor
                  | factor POWER expression
                   '''
    t[0] = OpNode(t[2], t[1], t[3])


def p_expr_uminus(t):
    'factor : MINUS expression %prec UMINUS'
    t[0] = NegateNode(t[2])

def p_EOP(t):
    '''expression : expression EOP expression'''
    t[0] = EOPNode(t[1], t[3])

def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]


def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]

def p_equal(t):
    '''
    boolean : expression EQUAL expression
        | expression NOTEQUAL expression
        | boolean EQUAL boolean
        | boolean NOTEQUAL boolean
    '''
    t[0] = IsEqualNode(t[2], t[1], t[3])

def p_comparison(t):
    '''
    boolean : expression GREATER factor
            | expression LESS factor
            | expression GREATEROREQUAL factor
            | expression LESSOREQUAL factor
            | expression EQUAL factor
            | STRING GREATER STRING
            | STRING LESS STRING
            | STRING GREATEROREQUAL STRING
            | STRING LESSOREQUAL STRING
            | STRING EQUAL STRING

    '''
    t[0] = ComparisonNode(t[2], t[1], t[3])

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

def p_list_elms(t):
    '''
    list_element : expression
        | STRING
        | boolean
    '''
    t[0] = ListNode(t[1])

def p_list_elms_cont(t):
    '''
    list_element : list_element expression
    | list_element STRING
    | list_element boolean
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_list_elms_comma(t):
    'list_element : list_element COMMA'
    t[0] = t[1]

def p_list(t):
    '''
    list : LBRACE list_element RBRACE
        | LBRACE RBRACE
    '''
    if(len(t) >= 4):
        t[0] = t[2]
    else:
        t[0] = ListNode(None)

def p_index(t):
    '''
    expression : list LBRACE expression RBRACE
        | STRING LBRACE expression RBRACE
    '''
    t[0] = t[1].get(t[3])

def p_cons(t):
    '''
    list : expression CONS list
        | boolean CONS list
        | STRING CONS list
        | list CONS list
    '''
    t[3].prepend(t[1])
    t[0] = t[3]

def p_in_list(t):
    '''
    boolean : expression IN list
        | boolean IN list
        | STRING IN list
        | list IN list
    '''
    t[0] = InList(t[1], t[3])

def p_error(t):
    print("SYNTAX ERROR")

yacc.yacc()


# file = open('testInput.txt', 'r')

file = open(sys.argv[1], 'r')

lines = file.readlines()
# print(lines)
code = ""
for line in lines:
    # if len(line) < 2: continue
    code = line.strip()
    try:
        lex.input(code)
        while True:
            token = lex.token()
            if not token: break
            # print(token)
        # print(code)
        # ast = yacc.parse(code, debug=1)
        ast = yacc.parse(code)

        ast.execute()
    except Exception:
        error = traceback.format_exc()
        print("ERROR")
    else:
        error = ""
    finally:
        print(error)
