
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLBRACERBRACEleftORleftANDleftNOTleftEQUALNOTEQUALGREATERGREATEROREQUALLESSLESSOREQUALleftPLUSMINUSleftTIMESDIVIDEDIVrightPOWERleftEOPrightUMINUSAND COMMA CONS DIV DIVIDE EOP EQUAL FALSE GREATER GREATEROREQUAL IN LBRACE LESS LESSOREQUAL LPAREN MINUS MOD NOT NOTEQUAL NUMBER OR PLUS POUND POWER PRINT RBRACE RPAREN SEMICOLON STRING TIMES TRUEstatement : expression SEMICOLON\n         | boolean SEMICOLON\n         | list SEMICOLON\n    statement : STRING SEMICOLON\n    \n    factor : LPAREN expression RPAREN\n    \n    expression : STRING PLUS STRING\n        | list PLUS list\n    expression : expression PLUS factor\n                  | expression MINUS factor\n                  | expression TIMES factor\n                  | expression DIVIDE factor\n                  | expression DIV factor\n                  | expression MOD factor\n                  | factor POWER expression\n                   factor : MINUS expression %prec UMINUSexpression : expression EOP expressionexpression : factorfactor : NUMBER\n    boolean : expression EQUAL expression\n        | expression NOTEQUAL expression\n        | boolean EQUAL boolean\n        | boolean NOTEQUAL boolean\n    \n    boolean : expression GREATER factor\n            | expression LESS factor\n            | expression GREATEROREQUAL factor\n            | expression LESSOREQUAL factor\n            | expression EQUAL factor\n            | STRING GREATER STRING\n            | STRING LESS STRING\n            | STRING GREATEROREQUAL STRING\n            | STRING LESSOREQUAL STRING\n            | STRING EQUAL STRING\n\n    \n    boolean : boolean AND boolean\n        | boolean OR boolean\n    boolean : NOT boolean\n    boolean : TRUE\n        | FALSE\n    \n    list_element : expression\n        | STRING\n        | boolean\n    \n    list_element : list_element expression\n    | list_element STRING\n    | list_element boolean\n    list_element : list_element COMMA\n    list : LBRACE list_element RBRACE\n        | LBRACE RBRACE\n    \n    expression : list LBRACE expression RBRACE\n        | STRING LBRACE expression RBRACE\n    \n    list : expression CONS list\n        | boolean CONS list\n        | STRING CONS list\n        | list CONS list\n    \n    boolean : expression IN list\n        | boolean IN list\n        | STRING IN list\n        | list IN list\n    '
    
_lr_action_items = {'STRING':([0,6,7,8,9,10,11,12,13,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[5,-17,54,60,65,-36,-37,54,-18,54,54,54,84,84,65,65,65,65,84,84,84,54,84,84,96,54,98,99,100,101,102,84,84,54,-15,108,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'NOT':([0,6,7,8,9,10,11,12,13,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[9,-17,9,9,9,-36,-37,9,-18,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-15,9,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'TRUE':([0,6,7,8,9,10,11,12,13,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[10,-17,10,10,10,-36,-37,10,-18,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-15,10,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'FALSE':([0,6,7,8,9,10,11,12,13,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[11,-17,11,11,11,-36,-37,11,-18,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-15,11,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'LBRACE':([0,4,5,6,7,8,9,10,11,12,13,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,54,55,57,58,59,60,61,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[8,39,44,-17,8,8,8,-36,-37,8,-18,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-15,44,39,8,-46,-38,44,-40,39,-35,44,39,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,39,44,39,-21,-22,-33,-34,39,39,-7,39,39,-6,-28,-29,-30,-31,-32,39,39,-14,-45,-41,44,-43,-44,-5,-47,-48,]),'LPAREN':([0,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[12,-17,12,12,12,-36,-37,12,-18,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-15,12,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'MINUS':([0,2,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,57,58,59,60,61,63,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[7,16,-17,7,7,7,-36,-37,7,-18,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-15,7,-46,16,-39,-40,-35,16,16,-8,-9,-10,-11,-12,-13,-16,16,-17,16,-23,-24,-25,-26,16,-53,-49,-21,-22,-33,-34,-54,-50,-7,16,-56,-52,-6,16,-28,-29,-30,-31,-32,-55,-51,-14,-45,16,-42,-43,-44,-5,-47,-48,]),'NUMBER':([0,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[13,-17,13,13,13,-36,-37,13,-18,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-15,13,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'$end':([1,14,30,37,42,],[0,-1,-2,-3,-4,]),'SEMICOLON':([2,3,4,5,6,10,11,13,53,58,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,111,112,113,],[14,30,37,42,-17,-36,-37,-18,-15,-46,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-5,-47,-48,]),'PLUS':([2,4,5,6,13,53,54,55,58,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,82,83,84,85,90,91,92,93,94,95,96,97,103,104,105,106,107,108,111,112,113,],[15,38,43,-17,-18,-15,43,38,-46,15,43,38,15,43,38,15,-8,-9,-10,-11,-12,-13,-16,15,-17,15,15,38,43,38,38,38,-7,15,38,38,-6,15,38,38,-14,-45,15,43,-5,-47,-48,]),'TIMES':([2,6,13,53,58,59,64,67,68,69,70,71,72,73,74,75,76,77,82,85,91,92,93,95,96,97,104,105,106,107,111,112,113,],[17,-17,-18,-15,-46,17,17,17,-8,-9,-10,-11,-12,-13,-16,17,-17,17,17,-49,-50,-7,17,-52,-6,17,-51,-14,-45,17,-5,-47,-48,]),'DIVIDE':([2,6,13,53,58,59,64,67,68,69,70,71,72,73,74,75,76,77,82,85,91,92,93,95,96,97,104,105,106,107,111,112,113,],[18,-17,-18,-15,-46,18,18,18,-8,-9,-10,-11,-12,-13,-16,18,-17,18,18,-49,-50,-7,18,-52,-6,18,-51,-14,-45,18,-5,-47,-48,]),'DIV':([2,6,13,53,58,59,64,67,68,69,70,71,72,73,74,75,76,77,82,85,91,92,93,95,96,97,104,105,106,107,111,112,113,],[19,-17,-18,-15,-46,19,19,19,-8,-9,-10,-11,-12,-13,-16,19,-17,19,19,-49,-50,-7,19,-52,-6,19,-51,-14,-45,19,-5,-47,-48,]),'MOD':([2,6,13,53,58,59,64,67,68,69,70,71,72,73,74,75,76,77,82,85,91,92,93,95,96,97,104,105,106,107,111,112,113,],[20,-17,-18,-15,-46,20,20,20,-8,-9,-10,-11,-12,-13,-16,20,-17,20,20,-49,-50,-7,20,-52,-6,20,-51,-14,-45,20,-5,-47,-48,]),'EOP':([2,6,13,53,58,59,64,67,68,69,70,71,72,73,74,75,76,77,82,85,91,92,93,95,96,97,104,105,106,107,111,112,113,],[21,-17,-18,-15,-46,21,21,21,-8,-9,-10,-11,-12,-13,-16,21,-17,21,21,-49,-50,-7,21,-52,-6,21,-51,21,-45,21,-5,-47,-48,]),'EQUAL':([2,3,5,6,10,11,13,53,54,56,58,59,60,61,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,],[22,31,49,-17,-36,-37,-18,-15,49,31,-46,22,49,31,31,22,49,22,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,22,-53,49,-49,-21,-22,31,31,-54,-50,-7,22,-56,-52,-6,22,-28,-29,-30,-31,-32,-55,-51,-14,-45,22,49,31,-5,-47,-48,]),'NOTEQUAL':([2,3,6,10,11,13,53,56,58,59,61,63,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,111,112,113,],[23,32,-17,-36,-37,-18,-15,32,-46,23,32,32,23,23,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,23,-53,-49,-21,-22,32,32,-54,-50,-7,23,-56,-52,-6,23,-28,-29,-30,-31,-32,-55,-51,-14,-45,23,32,-5,-47,-48,]),'GREATER':([2,5,6,13,53,54,58,59,60,64,65,67,68,69,70,71,72,73,74,75,76,77,82,84,85,91,92,93,95,96,97,104,105,106,107,108,111,112,113,],[24,45,-17,-18,-15,45,-46,24,45,24,45,24,-8,-9,-10,-11,-12,-13,-16,24,-17,24,24,45,-49,-50,-7,24,-52,-6,24,-51,-14,-45,24,45,-5,-47,-48,]),'LESS':([2,5,6,13,53,54,58,59,60,64,65,67,68,69,70,71,72,73,74,75,76,77,82,84,85,91,92,93,95,96,97,104,105,106,107,108,111,112,113,],[25,46,-17,-18,-15,46,-46,25,46,25,46,25,-8,-9,-10,-11,-12,-13,-16,25,-17,25,25,46,-49,-50,-7,25,-52,-6,25,-51,-14,-45,25,46,-5,-47,-48,]),'GREATEROREQUAL':([2,5,6,13,53,54,58,59,60,64,65,67,68,69,70,71,72,73,74,75,76,77,82,84,85,91,92,93,95,96,97,104,105,106,107,108,111,112,113,],[26,47,-17,-18,-15,47,-46,26,47,26,47,26,-8,-9,-10,-11,-12,-13,-16,26,-17,26,26,47,-49,-50,-7,26,-52,-6,26,-51,-14,-45,26,47,-5,-47,-48,]),'LESSOREQUAL':([2,5,6,13,53,54,58,59,60,64,65,67,68,69,70,71,72,73,74,75,76,77,82,84,85,91,92,93,95,96,97,104,105,106,107,108,111,112,113,],[27,48,-17,-18,-15,48,-46,27,48,27,48,27,-8,-9,-10,-11,-12,-13,-16,27,-17,27,27,48,-49,-50,-7,27,-52,-6,27,-51,-14,-45,27,48,-5,-47,-48,]),'IN':([2,3,4,5,6,10,11,13,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,],[28,35,40,50,-17,-36,-37,-18,-15,50,40,35,-46,28,50,35,40,-35,28,50,40,28,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,28,40,50,40,-21,-22,-33,-34,40,40,-7,28,40,40,-6,28,-28,-29,-30,-31,-32,40,40,-14,-45,28,50,35,-5,-47,-48,]),'CONS':([2,3,4,5,6,10,11,13,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,],[29,36,41,51,-17,-36,-37,-18,-15,51,41,36,-46,29,51,36,41,-35,29,51,41,29,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,29,41,51,41,-21,-22,-33,-34,41,41,-7,29,41,41,-6,29,-28,-29,-30,-31,-32,41,41,-14,-45,29,51,36,-5,-47,-48,]),'AND':([3,6,10,11,13,53,56,58,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,109,111,112,113,],[33,-17,-36,-37,-18,-15,33,-46,33,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,33,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,33,-5,-47,-48,]),'OR':([3,6,10,11,13,53,56,58,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,109,111,112,113,],[34,-17,-36,-37,-18,-15,34,-46,34,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,34,-5,-47,-48,]),'POWER':([6,13,53,58,68,69,70,71,72,73,74,76,85,91,92,95,96,104,105,106,111,112,113,],[52,-18,-15,-46,-8,-9,-10,-11,-12,-13,-16,52,-49,-50,-7,-52,-6,-51,-14,-45,-5,-47,-48,]),'RBRACE':([6,8,10,11,13,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[-17,58,-36,-37,-18,-15,106,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,112,-56,-52,-6,113,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'COMMA':([6,10,11,13,53,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,94,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,],[-17,-36,-37,-18,-15,110,-46,-38,-39,-40,-35,-8,-9,-10,-11,-12,-13,-16,-19,-17,-20,-23,-24,-25,-26,-53,-49,-21,-22,-33,-34,-54,-50,-7,-56,-52,-6,-28,-29,-30,-31,-32,-55,-51,-14,-45,-41,-42,-43,-44,-5,-47,-48,]),'RPAREN':([6,13,53,58,67,68,69,70,71,72,73,74,85,91,92,95,96,104,105,106,111,112,113,],[-17,-18,-15,-46,111,-8,-9,-10,-11,-12,-13,-16,-49,-50,-7,-52,-6,-51,-14,-45,-5,-47,-48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,7,8,9,12,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,57,],[2,53,59,64,67,74,75,77,82,82,64,64,64,64,82,82,82,93,82,82,97,82,82,105,107,]),'boolean':([0,7,8,9,12,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,57,],[3,56,61,63,56,56,56,56,56,56,86,87,88,89,56,56,56,56,56,56,56,56,56,56,109,]),'list':([0,7,8,9,12,21,22,23,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,57,],[4,55,62,66,55,55,55,55,83,85,66,66,66,66,90,91,92,55,94,95,55,103,104,55,62,]),'factor':([0,7,8,9,12,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,38,39,40,41,44,50,51,52,57,],[6,6,6,6,6,68,69,70,71,72,73,6,76,6,78,79,80,81,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'list_element':([8,],[57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_exp','sbml.py',298),
  ('statement -> boolean SEMICOLON','statement',2,'p_statement_exp','sbml.py',299),
  ('statement -> list SEMICOLON','statement',2,'p_statement_exp','sbml.py',300),
  ('statement -> STRING SEMICOLON','statement',2,'p_string_exp','sbml.py',305),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_parenthesis','sbml.py',312),
  ('expression -> STRING PLUS STRING','expression',3,'p_concat','sbml.py',318),
  ('expression -> list PLUS list','expression',3,'p_concat','sbml.py',319),
  ('expression -> expression PLUS factor','expression',3,'p_expression_op','sbml.py',324),
  ('expression -> expression MINUS factor','expression',3,'p_expression_op','sbml.py',325),
  ('expression -> expression TIMES factor','expression',3,'p_expression_op','sbml.py',326),
  ('expression -> expression DIVIDE factor','expression',3,'p_expression_op','sbml.py',327),
  ('expression -> expression DIV factor','expression',3,'p_expression_op','sbml.py',328),
  ('expression -> expression MOD factor','expression',3,'p_expression_op','sbml.py',329),
  ('expression -> factor POWER expression','expression',3,'p_expression_op','sbml.py',330),
  ('factor -> MINUS expression','factor',2,'p_expr_uminus','sbml.py',336),
  ('expression -> expression EOP expression','expression',3,'p_EOP','sbml.py',340),
  ('expression -> factor','expression',1,'p_expression_factor','sbml.py',344),
  ('factor -> NUMBER','factor',1,'p_factor_number','sbml.py',349),
  ('boolean -> expression EQUAL expression','boolean',3,'p_equal','sbml.py',354),
  ('boolean -> expression NOTEQUAL expression','boolean',3,'p_equal','sbml.py',355),
  ('boolean -> boolean EQUAL boolean','boolean',3,'p_equal','sbml.py',356),
  ('boolean -> boolean NOTEQUAL boolean','boolean',3,'p_equal','sbml.py',357),
  ('boolean -> expression GREATER factor','boolean',3,'p_comparison','sbml.py',363),
  ('boolean -> expression LESS factor','boolean',3,'p_comparison','sbml.py',364),
  ('boolean -> expression GREATEROREQUAL factor','boolean',3,'p_comparison','sbml.py',365),
  ('boolean -> expression LESSOREQUAL factor','boolean',3,'p_comparison','sbml.py',366),
  ('boolean -> expression EQUAL factor','boolean',3,'p_comparison','sbml.py',367),
  ('boolean -> STRING GREATER STRING','boolean',3,'p_comparison','sbml.py',368),
  ('boolean -> STRING LESS STRING','boolean',3,'p_comparison','sbml.py',369),
  ('boolean -> STRING GREATEROREQUAL STRING','boolean',3,'p_comparison','sbml.py',370),
  ('boolean -> STRING LESSOREQUAL STRING','boolean',3,'p_comparison','sbml.py',371),
  ('boolean -> STRING EQUAL STRING','boolean',3,'p_comparison','sbml.py',372),
  ('boolean -> boolean AND boolean','boolean',3,'p_boolean_op','sbml.py',379),
  ('boolean -> boolean OR boolean','boolean',3,'p_boolean_op','sbml.py',380),
  ('boolean -> NOT boolean','boolean',2,'p_boolean_not','sbml.py',385),
  ('boolean -> TRUE','boolean',1,'p_boolean','sbml.py',390),
  ('boolean -> FALSE','boolean',1,'p_boolean','sbml.py',391),
  ('list_element -> expression','list_element',1,'p_list_elms','sbml.py',397),
  ('list_element -> STRING','list_element',1,'p_list_elms','sbml.py',398),
  ('list_element -> boolean','list_element',1,'p_list_elms','sbml.py',399),
  ('list_element -> list_element expression','list_element',2,'p_list_elms_cont','sbml.py',405),
  ('list_element -> list_element STRING','list_element',2,'p_list_elms_cont','sbml.py',406),
  ('list_element -> list_element boolean','list_element',2,'p_list_elms_cont','sbml.py',407),
  ('list_element -> list_element COMMA','list_element',2,'p_list_elms_comma','sbml.py',413),
  ('list -> LBRACE list_element RBRACE','list',3,'p_list','sbml.py',418),
  ('list -> LBRACE RBRACE','list',2,'p_list','sbml.py',419),
  ('expression -> list LBRACE expression RBRACE','expression',4,'p_index','sbml.py',428),
  ('expression -> STRING LBRACE expression RBRACE','expression',4,'p_index','sbml.py',429),
  ('list -> expression CONS list','list',3,'p_cons','sbml.py',435),
  ('list -> boolean CONS list','list',3,'p_cons','sbml.py',436),
  ('list -> STRING CONS list','list',3,'p_cons','sbml.py',437),
  ('list -> list CONS list','list',3,'p_cons','sbml.py',438),
  ('boolean -> expression IN list','boolean',3,'p_in_list','sbml.py',445),
  ('boolean -> boolean IN list','boolean',3,'p_in_list','sbml.py',446),
  ('boolean -> STRING IN list','boolean',3,'p_in_list','sbml.py',447),
  ('boolean -> list IN list','boolean',3,'p_in_list','sbml.py',448),
]
