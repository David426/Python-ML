# David Sill 111486160
# Assigment HW 3 CSE 307

import ply.lex as lex
import ply.yacc as yacc
import sys

# ------------------------------------
# Building Lex
# ------------------------------------
lex.lex()
yacc.yacc()


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
    ast = yacc.parse(code)
    ast.execute()
except Exception:
    print("ERROR")