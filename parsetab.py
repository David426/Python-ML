
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLBRACERBRACEleftIDrightASSIGNMENTleftORleftANDleftNOTleftEQUALNOTEQUALGREATERGREATEROREQUALLESSLESSOREQUALleftCONSleftINleftPLUSMINUSleftTIMESDIVIDEDIVMODrightPOWERleftLIST_INDEXleftEOPrightUMINUSAND ASSIGNMENT COMMA CONS DIV DIVIDE ELSE EOP EQUAL FALSE GREATER GREATEROREQUAL ID IF IN LBRACE LESS LESSOREQUAL LPAREN L_CURLY MINUS MOD NOT NOTEQUAL NUMBER OR PLUS POUND POWER PRINT RBRACE RPAREN R_CURLY SEMICOLON STRING TIMES TRUE\n     block : L_CURLY statement_list R_CURLY\n    \n     statement_list : statement_list statement\n    \n    statement_list : statement\n    \n        statement : expression SEMICOLON\n    \n    expression : LPAREN expression RPAREN\n    \n    statement : PRINT LPAREN expression RPAREN SEMICOLON\n    expression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression DIV expression\n                  | expression MOD expression\n                  | expression POWER expression\n                   \n    boolean : expression GREATER expression\n            | expression LESS expression\n            | expression GREATEROREQUAL expression\n            | expression LESSOREQUAL expression\n            | expression EQUAL expression\n            | expression NOTEQUAL expression\n    \n    expression : expression AND expression\n    | expression OR expression\n    | NOT expression\n    \n    expression : expression CONS expression\n    \n    expression : expression LBRACE expression RBRACE %prec LIST_INDEX\n    \n    expression : expression IN expression\n    expression : factor\n    | STRING\n    | boolean\n    | list\n    | var\n    \n    var : ID\n    \n    var : ID ASSIGNMENT expression\n    \n    list_element : expression\n        | list_element expression\n    list_element : list_element COMMA\n    list : LBRACE list_element RBRACE\n        | LBRACE RBRACE\n    \n    boolean : TRUE\n        | FALSE\n    factor : MINUS factor %prec UMINUSexpression : expression EOP expressionfactor : NUMBER'
    
_lr_action_items = {'L_CURLY':([0,],[2,]),'$end':([1,20,],[0,-1,]),'PRINT':([2,3,4,21,22,77,],[6,6,-3,-2,-4,-6,]),'LPAREN':([2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[7,7,-3,42,7,7,7,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-40,-22,7,-37,-33,7,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'NOT':([2,3,4,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[9,9,-3,9,9,9,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-40,-22,9,-37,-33,9,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'STRING':([2,3,4,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[12,12,-3,12,12,12,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-40,-22,12,-37,-33,12,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'MINUS':([2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,],[8,8,-3,24,8,8,8,8,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,24,-40,24,8,-37,24,8,-7,-8,-9,-10,-11,-12,-13,24,24,24,24,24,-41,24,24,24,24,24,24,24,-5,-36,24,-35,24,-24,-6,]),'NUMBER':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[16,16,-3,16,16,16,16,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-40,-22,16,-37,-33,16,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'TRUE':([2,3,4,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[17,17,-3,17,17,17,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-40,-22,17,-37,-33,17,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'FALSE':([2,3,4,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[18,18,-3,18,18,18,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-40,-22,18,-37,-33,18,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'LBRACE':([2,3,4,5,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,],[10,10,-3,33,10,10,10,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,33,-40,-22,10,-37,33,10,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,33,-25,-41,-14,-15,-16,-17,-18,-19,33,-5,-36,33,-35,-32,-24,-6,]),'ID':([2,3,4,7,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,77,],[19,19,-3,19,19,19,-26,-27,-28,-29,-30,-42,-38,-39,-31,-2,-4,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-40,-22,19,-37,-33,19,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,-6,]),'R_CURLY':([3,4,21,22,77,],[20,-3,-2,-4,-6,]),'SEMICOLON':([5,11,12,13,14,15,16,17,18,19,44,45,47,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,74,75,76,],[22,-26,-27,-28,-29,-30,-42,-38,-39,-31,-40,-22,-37,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-32,-24,77,]),'PLUS':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[23,-26,-27,-28,-29,-30,-42,-38,-39,-31,23,-40,23,-37,23,-7,-8,-9,-10,-11,-12,-13,23,23,23,23,23,-41,23,23,23,23,23,23,23,-5,-36,23,23,-24,]),'TIMES':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[25,-26,-27,-28,-29,-30,-42,-38,-39,-31,25,-40,25,-37,25,25,25,-9,-10,-11,-12,-13,25,25,25,25,25,-41,25,25,25,25,25,25,25,-5,-36,25,25,-24,]),'DIVIDE':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[26,-26,-27,-28,-29,-30,-42,-38,-39,-31,26,-40,26,-37,26,26,26,-9,-10,-11,-12,-13,26,26,26,26,26,-41,26,26,26,26,26,26,26,-5,-36,26,26,-24,]),'DIV':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[27,-26,-27,-28,-29,-30,-42,-38,-39,-31,27,-40,27,-37,27,27,27,-9,-10,-11,-12,-13,27,27,27,27,27,-41,27,27,27,27,27,27,27,-5,-36,27,27,-24,]),'MOD':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[28,-26,-27,-28,-29,-30,-42,-38,-39,-31,28,-40,28,-37,28,28,28,-9,-10,-11,-12,-13,28,28,28,28,28,-41,28,28,28,28,28,28,28,-5,-36,28,28,-24,]),'POWER':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[29,-26,-27,-28,-29,-30,-42,-38,-39,-31,29,-40,29,-37,29,29,29,29,29,29,29,29,29,29,29,29,29,-41,29,29,29,29,29,29,29,-5,-36,29,29,-24,]),'AND':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[30,-26,-27,-28,-29,-30,-42,-38,-39,-31,30,-40,-22,-37,30,-7,-8,-9,-10,-11,-12,-13,-20,30,-23,30,-25,-41,-14,-15,-16,-17,-18,-19,30,-5,-36,30,30,-24,]),'OR':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[31,-26,-27,-28,-29,-30,-42,-38,-39,-31,31,-40,-22,-37,31,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,31,-25,-41,-14,-15,-16,-17,-18,-19,31,-5,-36,31,31,-24,]),'CONS':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[32,-26,-27,-28,-29,-30,-42,-38,-39,-31,32,-40,32,-37,32,-7,-8,-9,-10,-11,-12,-13,32,32,-23,32,-25,-41,32,32,32,32,32,32,32,-5,-36,32,32,-24,]),'IN':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[34,-26,-27,-28,-29,-30,-42,-38,-39,-31,34,-40,34,-37,34,-7,-8,-9,-10,-11,-12,-13,34,34,34,34,-25,-41,34,34,34,34,34,34,34,-5,-36,34,34,-24,]),'EOP':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[35,-26,-27,-28,-29,-30,-42,-38,-39,-31,35,-40,35,-37,35,35,35,35,35,35,35,35,35,35,35,35,35,-41,35,35,35,35,35,35,35,-5,-36,35,35,-24,]),'GREATER':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[36,-26,-27,-28,-29,-30,-42,-38,-39,-31,36,-40,36,-37,36,-7,-8,-9,-10,-11,-12,-13,36,36,-23,36,-25,-41,-14,-15,-16,-17,-18,-19,36,-5,-36,36,36,-24,]),'LESS':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[37,-26,-27,-28,-29,-30,-42,-38,-39,-31,37,-40,37,-37,37,-7,-8,-9,-10,-11,-12,-13,37,37,-23,37,-25,-41,-14,-15,-16,-17,-18,-19,37,-5,-36,37,37,-24,]),'GREATEROREQUAL':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[38,-26,-27,-28,-29,-30,-42,-38,-39,-31,38,-40,38,-37,38,-7,-8,-9,-10,-11,-12,-13,38,38,-23,38,-25,-41,-14,-15,-16,-17,-18,-19,38,-5,-36,38,38,-24,]),'LESSOREQUAL':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[39,-26,-27,-28,-29,-30,-42,-38,-39,-31,39,-40,39,-37,39,-7,-8,-9,-10,-11,-12,-13,39,39,-23,39,-25,-41,-14,-15,-16,-17,-18,-19,39,-5,-36,39,39,-24,]),'EQUAL':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[40,-26,-27,-28,-29,-30,-42,-38,-39,-31,40,-40,40,-37,40,-7,-8,-9,-10,-11,-12,-13,40,40,-23,40,-25,-41,-14,-15,-16,-17,-18,-19,40,-5,-36,40,40,-24,]),'NOTEQUAL':([5,11,12,13,14,15,16,17,18,19,43,44,45,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,],[41,-26,-27,-28,-29,-30,-42,-38,-39,-31,41,-40,41,-37,41,-7,-8,-9,-10,-11,-12,-13,41,41,-23,41,-25,-41,-14,-15,-16,-17,-18,-19,41,-5,-36,41,41,-24,]),'RBRACE':([10,11,12,13,14,15,16,17,18,19,44,45,46,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,],[47,-26,-27,-28,-29,-30,-42,-38,-39,-31,-40,-22,71,-37,-33,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,75,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,]),'RPAREN':([11,12,13,14,15,16,17,18,19,43,44,45,47,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,69,70,71,74,75,],[-26,-27,-28,-29,-30,-42,-38,-39,-31,70,-40,-22,-37,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,76,-5,-36,-32,-24,]),'COMMA':([11,12,13,14,15,16,17,18,19,44,45,46,47,48,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,70,71,72,73,74,75,],[-26,-27,-28,-29,-30,-42,-38,-39,-31,-40,-22,73,-37,-33,-7,-8,-9,-10,-11,-12,-13,-20,-21,-23,-25,-41,-14,-15,-16,-17,-18,-19,-5,-36,-34,-35,-32,-24,]),'ASSIGNMENT':([19,],[49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,],[1,]),'statement_list':([2,],[3,]),'statement':([2,3,],[4,21,]),'expression':([2,3,7,9,10,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,49,],[5,5,43,45,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,72,74,]),'factor':([2,3,7,8,9,10,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,49,],[11,11,11,44,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'boolean':([2,3,7,9,10,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,49,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'list':([2,3,7,9,10,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,49,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'var':([2,3,7,9,10,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,49,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'list_element':([10,],[46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> L_CURLY statement_list R_CURLY','block',3,'p_block','sbml.py',465),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','sbml.py',471),
  ('statement_list -> statement','statement_list',1,'p_statement_list_val','sbml.py',477),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','sbml.py',483),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_parentheses','sbml.py',489),
  ('statement -> PRINT LPAREN expression RPAREN SEMICOLON','statement',5,'p_print_statement','sbml.py',495),
  ('expression -> expression PLUS expression','expression',3,'p_expression_op','sbml.py',500),
  ('expression -> expression MINUS expression','expression',3,'p_expression_op','sbml.py',501),
  ('expression -> expression TIMES expression','expression',3,'p_expression_op','sbml.py',502),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_op','sbml.py',503),
  ('expression -> expression DIV expression','expression',3,'p_expression_op','sbml.py',504),
  ('expression -> expression MOD expression','expression',3,'p_expression_op','sbml.py',505),
  ('expression -> expression POWER expression','expression',3,'p_expression_op','sbml.py',506),
  ('boolean -> expression GREATER expression','boolean',3,'p_comparison','sbml.py',512),
  ('boolean -> expression LESS expression','boolean',3,'p_comparison','sbml.py',513),
  ('boolean -> expression GREATEROREQUAL expression','boolean',3,'p_comparison','sbml.py',514),
  ('boolean -> expression LESSOREQUAL expression','boolean',3,'p_comparison','sbml.py',515),
  ('boolean -> expression EQUAL expression','boolean',3,'p_comparison','sbml.py',516),
  ('boolean -> expression NOTEQUAL expression','boolean',3,'p_comparison','sbml.py',517),
  ('expression -> expression AND expression','expression',3,'p_boolean_op','sbml.py',523),
  ('expression -> expression OR expression','expression',3,'p_boolean_op','sbml.py',524),
  ('expression -> NOT expression','expression',2,'p_boolean_op','sbml.py',525),
  ('expression -> expression CONS expression','expression',3,'p_cons','sbml.py',534),
  ('expression -> expression LBRACE expression RBRACE','expression',4,'p_index','sbml.py',540),
  ('expression -> expression IN expression','expression',3,'p_in_list','sbml.py',546),
  ('expression -> factor','expression',1,'p_expression','sbml.py',551),
  ('expression -> STRING','expression',1,'p_expression','sbml.py',552),
  ('expression -> boolean','expression',1,'p_expression','sbml.py',553),
  ('expression -> list','expression',1,'p_expression','sbml.py',554),
  ('expression -> var','expression',1,'p_expression','sbml.py',555),
  ('var -> ID','var',1,'p_variable','sbml.py',560),
  ('var -> ID ASSIGNMENT expression','var',3,'p_initialization','sbml.py',572),
  ('list_element -> expression','list_element',1,'p_list_elms','sbml.py',585),
  ('list_element -> list_element expression','list_element',2,'p_list_elms','sbml.py',586),
  ('list_element -> list_element COMMA','list_element',2,'p_list_elms_comma','sbml.py',595),
  ('list -> LBRACE list_element RBRACE','list',3,'p_list','sbml.py',600),
  ('list -> LBRACE RBRACE','list',2,'p_list','sbml.py',601),
  ('boolean -> TRUE','boolean',1,'p_boolean','sbml.py',610),
  ('boolean -> FALSE','boolean',1,'p_boolean','sbml.py',611),
  ('factor -> MINUS factor','factor',2,'p_expr_uminus','sbml.py',616),
  ('expression -> expression EOP expression','expression',3,'p_EOP','sbml.py',620),
  ('factor -> NUMBER','factor',1,'p_factor_number','sbml.py',624),
]
