# David Sill 111486160
# Assigment HW 3 CSE 307

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class BlockNode(Node):
    def __init__(self, sl):
        self.statementList = sl

    def evaluate(self):
        for statement in self.statementList:
            statement.evaluate()

class IfNode(Node):
    def __init__(self, condition, true_block, false_block):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block
    def evaluate(self):
        if self.condition.evaluate():
            self.true_block.evaluate()
        else:
            self.false_block.evaluate()

class PrintNode(Node):
    def __init__(self, e):
        self.e = e
    def evaluate(self):
        print(self.e.evaluate())

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
        if isinstance(self.value, str):
            print('\'' + self.value + '\'')
        else:
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
        # print("Item: " + self.item.__str__ + " List: " + self.list.__str__)
        return self.item.evaluate() in self.list.evaluate()

class VariableNode(Node):
    def __init__(self, id):
        self.id = id
        self.v = None
        self.initialized = False

    def assign_value(self, v):
        self.initialized = True
        self.v = v
    def is_initialized(self):
        return self.initialized

    def evaluate(self):
        if self.is_initialized():
            return self.v.evaluate()
        else:
            p_semantic_error(self)

import ply.lex as lex
import ply.yacc as yacc
import sys
import traceback
import string

# ------------------------------------
#           Building Lex
# ------------------------------------

reserved = {
    'mod' : 'MOD',
    'andalso' : 'AND',
    'orelse' : 'OR',
    'in' : 'IN',
    'not' : 'NOT',
    'True': 'TRUE',
    'False' : 'FALSE',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : "ELSE"
 }

tokens = [
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'R_CURLY', 'L_CURLY', 'COMMA', 'SEMICOLON',
    'NUMBER', 'EOP', 'STRING', 'ID', 'ASSIGNMENT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'DIV', 'POWER', 'CONS', 'POUND',
    'GREATER', 'LESS', 'EQUAL', 'GREATEROREQUAL', 'LESSOREQUAL', 'NOTEQUAL'
] + list(reserved.values())

#Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_L_CURLY = r'\{'
t_R_CURLY = r'\}'
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
t_ASSIGNMENT = r'='


def t_ID(t):
    '[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

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
    # ('left', 'L_CURLY', 'R_CURLY'),
    ('left', 'LBRACE', 'RBRACE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'EQUAL', 'NOTEQUAL', 'GREATER', 'GREATEROREQUAL', 'LESS', 'LESSOREQUAL'),
    ('left', 'CONS'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIV', 'MOD'),
    ('right', 'POWER'),
    ('left', 'LIST_INDEX'),
    ('left', 'EOP'),
    # ('right', 'PARENTHESIS'),
    ('right', 'UMINUS')
)

# def p_if_statement(p):
#     '''statement : IF LPAREN boolean RPAREN R_BRACE stat '''
#     # p[0] = IfNode(p[3], p[5], p[7])
#     p[0] = p[0]


def p_block(p):
    '''
     block : L_CURLY statement_list R_CURLY
    '''
    p[0] = BlockNode(p[2])


def p_statement_list(p):
    '''
     statement_list : statement_list statement
    '''
    p[0] = p[1] + [p[2]]

def p_statement_list_val(p):
    '''
    statement_list : statement
    '''
    p[0] = [p[1]]

def p_print_statement(p) :
    '''
    statement : PRINT LPAREN expression RPAREN SEMICOLON
    '''
    p[0] = PrintNode(p[3])

# def p_statement_exp(t):
#     '''statement : expression SEMICOLON
#          | boolean SEMICOLON
#          | list SEMICOLON
#          | variable SEMICOLON
#     '''
#     t[0] = ExecuteStatmentNode(t[1])
#
# def p_string_exp(t):
#     '''statement : string_exp SEMICOLON
#     '''
#
#     t[0] = ExecuteStatmentNode(t[1])

def p_parenthesis(t):
    '''
    expression : LPAREN expression RPAREN
    string_exp : LPAREN string_exp RPAREN
    '''
    t[0] = t[2]

def p_concat(t):
    '''
    string_exp : string_exp PLUS string_exp
    list :  list PLUS list
    '''
    t[0] = ConcatNode(t[1], t[3])

def p_string_expression(t):
    'string_exp : STRING'
    t[0] = t[1]

def p_expression_op(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POWER expression
                   '''
    t[0] = OpNode(t[2], t[1], t[3])


def p_expr_uminus(t):
    'factor : MINUS expression %prec UMINUS'
    t[0] = NegateNode(t[2])

def p_EOP(t):
    '''expression : expression EOP expression'''
    t[0] = EOPNode(t[1], t[3])

def p_expression(t):
    '''expression : factor
        | variable
    '''
    t[0] = t[1]


def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]

def p_equal(t):
    '''
    boolean : boolean EQUAL boolean
        | boolean NOTEQUAL boolean
    '''
    t[0] = IsEqualNode(t[2], t[1], t[3])

def p_comparison(t):
    '''
    boolean : expression GREATER expression
            | expression LESS expression
            | expression GREATEROREQUAL expression
            | expression LESSOREQUAL expression
            | expression EQUAL expression
            | expression NOTEQUAL expression
            | string_exp GREATER string_exp
            | string_exp LESS string_exp
            | string_exp GREATEROREQUAL string_exp
            | string_exp LESSOREQUAL string_exp
            | string_exp EQUAL string_exp
            | string_exp NOTEQUAL string_exp
    '''
    t[0] = ComparisonNode(t[2], t[1], t[3])

# def p_expression_str_exp(t):
#     'expression : string_exp'
#     t[0] = t[1]

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
        | string_exp
        | boolean
        | list
    '''
    t[0] = ListNode(t[1])

def p_list_elms_cont(t):
    '''
    list_element : list_element expression
    | list_element string_exp
    | list_element boolean
    | list_element list
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
    expression : list LBRACE expression RBRACE %prec LIST_INDEX
        | string_exp LBRACE expression RBRACE %prec LIST_INDEX
        | expression LBRACE expression RBRACE %prec LIST_INDEX
    '''
    if isinstance(t[1], ListNode) or isinstance(t[1], StringNode):
        t[0] = t[1].get(t[3])
    else:
        p_error(t)

def p_cons(t):
    '''
    list : expression CONS list
        | boolean CONS list
        | string_exp CONS list
        | list CONS list
    '''
    t[3].prepend(t[1])
    t[0] = t[3]

def p_in_list(t):
    '''
    boolean : expression IN list
        | boolean IN list
        | string_exp IN list
        | STRING IN list
        | list IN list
        | string_exp IN string_exp
        | STRING IN STRING
        | expression IN STRING
    '''
    if not isinstance(t[3], StringNode) or isinstance(t[1], StringNode):
        t[0] = InList(t[1], t[3])
    else:
        p_error(t)

def p_assign_variable(t):
    '''
    variable : ID ASSIGNMENT expression
        | ID ASSIGNMENT list
        | ID ASSIGNMENT string_exp
        | ID ASSIGNMENT boolean
        | ID ASSIGNMENT variable
    '''
    t[1].assign_value(t[3])
    t[0] = t[1]

def p_error(t):
    print("SYNTAX ERROR")
    return

def p_semantic_error(t):
    print("SEMANTIC ERROR")

yacc.yacc()

with open(sys.argv[1], 'r') as myfile:
    data = myfile.read().replace('\n', '')
# lex.input(data)
root = yacc.parse(data, debug=0)
root.evaluate()

# file = open(sys.argv[1], 'r')
# file = open('Tests/input_18.txt', 'r')

# lines = file.readlines()
# # print(lines)
# code = ""
# debug_toke_list = []
# for line in lines:
#     code = line.strip()
#     try:
#         lex.input(code)
#         while True:
#             token = lex.token()
#             debug_toke_list.append(token)
#             if not token: break
#     except Exception:
#         error = traceback.format_exc()
#         # print("ERROR")
#     else:
#         error = ""
#     finally:
#         ast = yacc.parse(code, debug=0)
#         ast.execute()
