# David Sill
# 111486160
# CSE 307

# -------------------------------------------
#               Nodes
# -------------------------------------------

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


class ExecuteStatmentNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):
        self.value = self.value.evaluate()
        if isinstance(self.value, str):
            print('\'' + self.value + '\'')
        else:
            print(self.value)


class ParenNode(Node):
    def __init__(self, exp):
        self.expression = exp
        self.return_type = self.expression.return_type

    def evaluate(self):
        return self.expression.evaluate()


class PrintNode(Node):
    def __init__(self, e):
        self.e = e

    def evaluate(self):
        print(self.e.evaluate())


class OpNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op
        if not self.v1.return_type is self.v2.return_type:
            raise SyntaxException("Mixed Operands")
        self.return_type = v1.return_type

    def evaluate(self):
        if self.op == '+':
            return self.plus()
        elif self.op == '-':
            return self.minus()
        elif self.op == '*':
            return self.multiply()
        elif self.op == '/':
            return self.divide()
        elif self.op == 'div':
            return self.div()
        elif self.op == 'mod':
            return self.mod
        elif self.op == '**':
            return self.power()

    def plus(self):
        # if isinstance(self.v1.return_type, (NumberNode, StringNode)):
        if self.v1.return_type is NumberNode or StringNode or ListNode:
            return self.v1.evaluate() + self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use +")

    def minus(self):
        if self.v1.return_type is NumberNode:
            return self.v1.evaluate() - self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use -")

    def multiply(self):
        if self.v1.return_type is NumberNode:
            return self.v1.evaluate() * self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use *")

    def divide(self):
        if self.v1.return_type is NumberNode:
            return self.v1.evaluate() / self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use /")

    def div(self):
        if self.v1.return_type is NumberNode:
            return self.v1.evaluate() // self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use div")

    def mod(self):
        if self.v1.return_type is NumberNode:
            return self.v1.evaluate() % self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use mod")

    def power(self):
        if self.v1.return_type is NumberNode:
            return self.v1.evaluate() ** self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use **")


class ComparisonNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

        if not self.v1.return_type is self.v2.return_type:
            raise SyntaxException("Mixed Operands")
        self.return_type = BooleanNode

    def evaluate(self):
        if self.op == '>':
            return self.greater()
        elif self.op == '<':
            return self.less()
        elif self.op == '>=':
            return self.greater_or_equal()
        elif self.op == '<=':
            return self.less_or_equal()
        elif self.op == '==':
            return self.equal()

    def greater(self):
        if self.v1.return_type is NumberNode or StringNode:
            return self.v1.evaluate() > self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use >")

    def less(self):
        if self.v1.return_type is NumberNode or StringNode:
            return self.v1.evaluate() < self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use <")

    def greater_or_equal(self):
        if self.v1.return_type is NumberNode or StringNode:
            return self.v1.evaluate() >= self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use >=")

    def less_or_equal(self):
        if self.v1.return_type is NumberNode or StringNode:
            return self.v1.evaluate() <= self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use <=")

    def equal(self):
        if self.v1.return_type is NumberNode or StringNode:
            return self.v1.evaluate() == self.v2.evaluate()
        else:
            raise SyntaxException("Operands Cannot use ==")

class BooleanOpNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op
        self.return_type = BooleanNode
        if not (self.v1.return_type is BooleanNode and self.v2.return_type is BooleanNode):
            raise SyntaxException("Cannot AND or OR non-boolean")

    def evaluate(self):
        if self.op == 'andalso':
            return self.v1.evaluate() and self.v2.evaluate()
        elif self.op == 'orelse':
            return self.v1.evaluate() or self.v2.evaluate()

class NotOpNode(Node):
    def __init__(self, v1):
        self.v1 = v1
        self.return_type = BooleanNode
        if not self.v1.return_type is BooleanNode:
            raise SyntaxException("NOT expects boolean")

    def evaluate(self):
        return not self.v1.evaluate

class ConsNode(Node):
    def __init__(self, item, list):
        self.item = item
        self.list = list
        self.return_type = ListNode
        if not self.list.return_type is ListNode:
            raise SyntaxException("CONS Expects list")
    def evaluate(self):
        # return self.list.evaluate().insert(0, self.item.evaluate())
        self.list.prepend(self.item)
        return self.list.evaluate()

class InListNode(Node):

    def __init__(self, item, list):
        self.item = item
        self.list = list
        self.return_type = BooleanNode
        if not (self.list.return_type is ListNode or StringNode):
            raise SyntaxException("Cannont IN non-list/string ")
    def evaluate(self):

        return self.item.evaluate() in self.list.evaluate()

class IndexNode(Node):
    def __init__(self, list, index):
        self.list = list
        self.index = index
        self.return_type = self.get_type()
        if not (self.list.return_type is ListNode or StringNode):
            raise SyntaxException("Cannont index ")

    def evaluate(self):
        return self.list.evaluate()[self.index.evaluate()]

    def get_type(self):
        return (self.list.get(self.index)).return_type


class ListNode(Node):
    def __init__(self, v):
        if v is not None:
            self.v = [v]
        else:
            self.v = []
        self.return_type = ListNode

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


class NumberNode(Node):
    def __init__(self, v):
        if ('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)
        self.return_type = NumberNode

    def evaluate(self):
        return self.value

class NegateNode(Node):
    def __init__(self, v):
        self.value = v
        self.return_type = NumberNode
    def evaluate(self):
        return self.value.evaluate() * -1


class EOPNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.return_type = NumberNode
    def evaluate(self):
        return self.v1.evaluate() * (10 ** self.v2.evaluate())


class BooleanNode(Node):
    def __init__(self, v):
        if 'True' == v:
            self.value = True
        else:
            self.value = False
        self.return_type = BooleanNode

    def evaluate(self):
        return self.value


class StringNode(Node):
    def __init__(self, v):
        if v[0] == '\'' or v[0] == '\"':
            self.v = v[1:len(v) - 1]
        else:
            self.v = v
        self.return_type = StringNode

    def output(self):
        return '\'' + self.value + '\''

    def get(self, index):
        return StringNode(self.v[index.evaluate()])

    def evaluate(self):
        return self.v


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


# ------------------------------------
#           Building Lex
# ------------------------------------
reserved = {
    'mod': 'MOD',
    'div': 'DIV',
    'andalso': 'AND',
    'orelse': 'OR',
    'in': 'IN',
    'not': 'NOT',
    'True': 'TRUE',
    'False': 'FALSE',
    'print': 'PRINT',
    'if': 'IF',
    'else': "ELSE",
    'e':"EOP"
}

tokens = [
             'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'R_CURLY', 'L_CURLY', 'COMMA', 'SEMICOLON',
             'NUMBER', 'STRING', 'ID', 'ASSIGNMENT',
             'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'CONS', 'POUND',
             'GREATER', 'LESS', 'EQUAL', 'GREATEROREQUAL', 'LESSOREQUAL', 'NOTEQUAL'
         ] + list(reserved.values())

# Tokens
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
t_POWER = r'\*\*'
t_CONS = r'::'
t_POUND = r'\#'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL = r'=='
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_NOTEQUAL = r'<>'
# t_EOP = r'e'
t_ASSIGNMENT = r'='

def t_RESERVED(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# def t_VARIABLE(t):
#     r'[A-Za-z][A-Za-z0-9_]*'
#     t.value = StringNode(t.value)
#     # print("yay")

def t_STRING(t):
    r'\"([^\"\'])*\"|\'([^\'\"])*\''
    t.value = StringNode(t.value)
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


# -------------------------------------------
#               Parsing
# -------------------------------------------

precedence = (
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
    ('right', 'UMINUS')
)


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


def p_statement(p):
    '''
        statement : expression
    '''
    p[0] = [p[1]]

def p_parentheses(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = ParenNode(p[2])

def p_print_statement(p):
    '''
    statement : PRINT LPAREN expression RPAREN SEMICOLON
    '''
    p[0] = PrintNode(p[3])


def p_expression_op(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POWER expression
                   '''
    p[0] = OpNode(p[2], p[1], p[3])


def p_comparison(p):
    '''
    boolean : expression GREATER expression
            | expression LESS expression
            | expression GREATEROREQUAL expression
            | expression LESSOREQUAL expression
            | expression EQUAL expression
            | expression NOTEQUAL expression
    '''
    p[0] = ComparisonNode(p[2], p[1], p[3])

def p_boolean_op(p):
    '''
    expression : expression AND expression
    | expression OR expression
    | NOT expression
    '''
    if len(p) == 4:
        p[0] = BooleanOpNode(p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = NotOpNode(p[2])

def p_cons(p):
    '''
    expression : expression CONS expression
    '''
    p[0] = ConsNode(p[1], p[3])

def p_index(p):
    '''
    expression : expression LBRACE expression RBRACE %prec LIST_INDEX
    '''
    p[0] = IndexNode(p[1], p[3])

def p_in_list(p):
    '''
    expression : expression IN expression
    '''
    p[0] = InListNode(p[1], p[3])


def p_expression(p):
    '''expression : factor
    | STRING
    | boolean
    | list
    '''
    p[0] = p[1]


def p_list_elms(p):
    '''
    list_element : expression
        | list_element expression
    '''
    if len(p) == 2:
        p[0] = ListNode(p[1])
    elif len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]


def p_list_elms_comma(p):
    'list_element : list_element COMMA'
    p[0] = p[1]


def p_list(p):
    '''
    list : LBRACE list_element RBRACE
        | LBRACE RBRACE
    '''
    if (len(p) >= 4):
        p[0] = p[2]
    else:
        p[0] = ListNode(None)


def p_boolean(p):
    '''
    boolean : TRUE
        | FALSE
    '''
    p[0] = BooleanNode(p[1])

def p_expr_uminus(t):
    'factor : MINUS factor %prec UMINUS'
    t[0] = NegateNode(t[2])

def p_EOP(t):
    '''expression : expression EOP expression'''
    t[0] = EOPNode(t[1], t[3])

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_error(t):
    print("SYNTAX ERROR")
    return


def p_semantic_error(t):
    print("SEMANTIC ERROR")



# -------------------------------------------
#               Main
# -------------------------------------------

import ply.yacc
import ply.lex
import sys


class SemanticException(Exception):
    def __init__(self, message):
        self.message = message

    pass


class SyntaxException(Exception):
    def __init__(self, message):
        self.message = message

    pass


lex = ply.lex.lex()
yacc = ply.yacc.yacc()

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = fd.read()

try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
    ast = yacc.parse(code, debug=1)
    ast.evaluate()
except SemanticException as err:
    print("SEMANTIC ERROR")
except SyntaxException as err:
    print("SYNTAX ERROR")
    print(err.message)
