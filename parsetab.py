
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'


_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND ASSIGN BREAK CBRACELET CLOSEBR COMMA DIVIDE DIVIDE_ASSIGN DO ELSE EQUALS FALSE FLOAT FLOAT_NUMBER FOR ID IF INT LARGE LARGETHAN LESS LESSTHAN LPAREN MINUS MINUSMINUS MINUS_ASSIGN NOTEQUAL NUMBER OBRACELET OPENBR PLUS PLUSPLUS PLUS_ASSIGN RPAREN SEMICOLON STRING TIMES TIMES_ASSIGN TRUE VOID WHILEprogram : declaration_listdeclaration_list : declaration_list declarationdeclaration_list : declarationdeclaration : var_declarationdeclaration : fun_declarationvar_declaration : type_specifier var_decl_list SEMICOLONvar_declaration : type_specifier error SEMICOLONvar_decl_list : var_decl_list COMMA var_decl_idvar_decl_list : var_decl_idvar_decl_id : IDvar_decl_id : ID OPENBR NUMBER CLOSEBRvar_decl_id : ID ASSIGN ID\n        | ID ASSIGN NUMBER\n        | ID ASSIGN FLOAT_NUMBER\n        | ID ASSIGN STRINGtype_specifier : INT\n    | FLOAT\n    | VOID\n    | STRINGfun_declaration : type_specifier ID LPAREN params RPAREN statementparams : param_listparams : param_list : param_list COMMA param_type_list param_list : param_type_listparam_type_list : type_specifier param_id_listparam_id_list : param_id_list COMMA param_idparam_id_list : param_idparam_id : IDcompound_stmt : OBRACELET local_declarations statement_list local_declarations CBRACELETlocal_declarations : local_declarations var_declarationlocal_declarations :statement_list : statement statement_liststatement_list :statement : expression_stmt\n    | compound_stmt\n    | if_stmt\n    | while_stmt\n    | for_stmt\n    | do_while_stmt\n    | break_stmtexpression_stmt : expression SEMICOLONexpression_stmt : SEMICOLONdo_while_stmt : do statement while LPAREN expression RPARENdo : DOif_stmt : if LPAREN expression RPAREN statementif_stmt : if LPAREN expression RPAREN statement else statementif : IFelse : ELSE while_stmt : while LPAREN expression RPAREN statementwhile : WHILEfor_stmt : for LPAREN var_declaration expression semicolon expression epsilon RPAREN statementsemicolon : SEMICOLONepsilon :for : FORbreak_stmt : BREAK SEMICOLON expression : var ASSIGN expression\n      | var addopration_expression expression\n      | var mulopration_expression expression \n      | ID PLUSPLUS\n      | ID MINUSMINUS\n      expression : simple_expression  addopration_expression : PLUS_ASSIGN\n    | MINUS_ASSIGN mulopration_expression : TIMES_ASSIGN\n    | DIVIDE_ASSIGNvar : IDvar : ID OPENBR NUMBER CLOSEBRsimple_expression : simple_expression AND unary_rel_expressionsimple_expression : unary_rel_expressionunary_rel_expression : NOTEQUAL unary_rel_expressionunary_rel_expression : rel_expressionrel_expression :  add_expression relop add_expression rel_expression : add_expressionrelop : EQUALS\n                  | LESS\n                  | LARGE\n                  | LARGETHAN\n                  | LESSTHAN\n                  | NOTEQUALadd_expression : add_expression addop term add_expression : termaddop : PLUS\n            | MINUS\n            term : term mulop unary_expression term : unary_expressionmulop : TIMES\n            | DIVIDEunary_expression : addop unary_expressionunary_expression : factorfactor : LPAREN expression RPAREN \n    | var \n    | call \n    | constantconstant : TRUE \n    | FALSEconstant : NUMBER constant : FLOAT_NUMBER call : ID LPAREN args RPARENargs : args_list\n    |args_list : args_list COMMA expression\n    | expression'
    
_lr_action_items = {'INT':([0,2,3,4,5,11,16,18,19,37,42,43,44,45,46,47,48,49,51,52,87,88,91,93,122,123,124,140,141,147,148,149,156,157,160,],[7,7,-3,-4,-5,-2,-6,-7,7,7,-20,-34,-35,-36,-37,-38,-39,-40,-42,-31,-41,7,7,-55,-31,-30,-33,7,-32,-29,-45,-49,-43,-46,-51,]),'FLOAT':([0,2,3,4,5,11,16,18,19,37,42,43,44,45,46,47,48,49,51,52,87,88,91,93,122,123,124,140,141,147,148,149,156,157,160,],[8,8,-3,-4,-5,-2,-6,-7,8,8,-20,-34,-35,-36,-37,-38,-39,-40,-42,-31,-41,8,8,-55,-31,-30,-33,8,-32,-29,-45,-49,-43,-46,-51,]),'VOID':([0,2,3,4,5,11,16,18,19,37,42,43,44,45,46,47,48,49,51,52,87,88,91,93,122,123,124,140,141,147,148,149,156,157,160,],[9,9,-3,-4,-5,-2,-6,-7,9,9,-20,-34,-35,-36,-37,-38,-39,-40,-42,-31,-41,9,9,-55,-31,-30,-33,9,-32,-29,-45,-49,-43,-46,-51,]),'STRING':([0,2,3,4,5,11,16,18,19,21,37,42,43,44,45,46,47,48,49,51,52,87,88,91,93,122,123,124,140,141,147,148,149,156,157,160,],[10,10,-3,-4,-5,-2,-6,-7,10,32,10,-20,-34,-35,-36,-37,-38,-39,-40,-42,-31,-41,10,10,-55,-31,-30,-33,10,-32,-29,-45,-49,-43,-46,-51,]),'$end':([1,2,3,4,5,11,16,18,42,43,44,45,46,47,48,49,51,87,93,147,148,149,156,157,160,],[0,-1,-3,-4,-5,-2,-6,-7,-20,-34,-35,-36,-37,-38,-39,-40,-42,-41,-55,-29,-45,-49,-43,-46,-51,]),'error':([6,7,8,9,10,125,],[13,-16,-17,-18,-19,13,]),'ID':([6,7,8,9,10,16,17,18,21,24,36,39,41,43,44,45,46,47,48,49,51,52,56,63,66,69,73,74,85,87,88,89,90,93,94,95,96,97,98,99,100,101,105,106,107,108,109,110,111,112,114,115,116,123,124,125,128,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[14,-16,-17,-18,-19,-6,23,-7,29,35,40,35,40,-34,-35,-36,-37,-38,-39,-40,-42,-31,40,-44,104,104,-82,-83,40,-41,40,40,40,-55,40,40,40,-62,-63,-64,-65,104,104,104,-74,-75,-76,-77,-78,-79,104,-86,-87,-30,40,23,40,40,40,40,40,-29,-45,-49,40,-52,40,-48,-43,-46,40,-51,]),'SEMICOLON':([12,13,14,15,16,18,22,23,29,30,31,32,36,38,40,43,44,45,46,47,48,49,50,51,52,56,57,58,59,63,64,65,67,68,70,71,72,75,76,77,78,79,82,83,87,88,93,102,103,104,113,121,123,124,130,131,132,133,134,135,136,137,138,142,143,144,147,148,149,153,154,156,157,159,160,],[16,18,-10,-9,-6,-7,-8,-10,-12,-13,-14,-15,51,-11,-66,-34,-35,-36,-37,-38,-39,-40,87,-42,-31,51,93,-91,-61,-44,-96,-69,-71,-73,-81,-85,-89,-92,-93,-94,-95,-97,-59,-60,-41,51,-55,-70,-91,-66,-88,-90,-30,51,-56,-57,-58,-68,-72,-80,-84,-67,-98,51,51,151,-29,-45,-49,51,-48,-43,-46,51,-51,]),'COMMA':([12,14,15,22,23,26,27,29,30,31,32,33,34,35,38,40,58,59,64,65,67,68,70,71,72,75,76,77,78,79,80,81,82,83,102,103,104,113,119,120,121,130,131,132,133,134,135,136,137,138,146,],[17,-10,-9,-8,-10,37,-24,-12,-13,-14,-15,39,-27,-28,-11,-66,-91,-61,-96,-69,-71,-73,-81,-85,-89,-92,-93,-94,-95,-97,-23,-26,-59,-60,-70,-91,-66,-88,139,-102,-90,-56,-57,-58,-68,-72,-80,-84,-67,-98,-101,]),'LPAREN':([14,16,18,36,40,41,43,44,45,46,47,48,49,51,52,53,54,55,56,60,61,62,63,66,69,73,74,85,87,88,89,90,93,94,95,96,97,98,99,100,101,104,105,106,107,108,109,110,111,112,114,115,116,123,124,128,129,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[19,-6,-7,41,85,41,-34,-35,-36,-37,-38,-39,-40,-42,-31,89,90,91,41,-47,-50,-54,-44,41,41,-82,-83,41,-41,41,41,41,-55,41,41,41,-62,-63,-64,-65,41,85,41,41,-74,-75,-76,-77,-78,-79,41,-86,-87,-30,41,41,145,41,41,41,41,-29,-45,-49,41,-52,41,-48,-43,-46,41,-51,]),'OPENBR':([14,23,40,104,],[20,20,84,84,]),'ASSIGN':([14,23,40,58,137,],[21,21,-66,94,-67,]),'OBRACELET':([16,18,36,43,44,45,46,47,48,49,51,52,56,63,87,88,93,123,124,142,143,147,148,149,153,154,156,157,159,160,],[-6,-7,52,-34,-35,-36,-37,-38,-39,-40,-42,-31,52,-44,-41,52,-55,-30,52,52,52,-29,-45,-49,52,-48,-43,-46,52,-51,]),'BREAK':([16,18,36,43,44,45,46,47,48,49,51,52,56,63,87,88,93,123,124,142,143,147,148,149,153,154,156,157,159,160,],[-6,-7,57,-34,-35,-36,-37,-38,-39,-40,-42,-31,57,-44,-41,57,-55,-30,57,57,57,-29,-45,-49,57,-48,-43,-46,57,-51,]),'IF':([16,18,36,43,44,45,46,47,48,49,51,52,56,63,87,88,93,123,124,142,143,147,148,149,153,154,156,157,159,160,],[-6,-7,60,-34,-35,-36,-37,-38,-39,-40,-42,-31,60,-44,-41,60,-55,-30,60,60,60,-29,-45,-49,60,-48,-43,-46,60,-51,]),'WHILE':([16,18,36,43,44,45,46,47,48,49,51,52,56,63,87,88,92,93,123,124,142,143,147,148,149,153,154,156,157,159,160,],[-6,-7,61,-34,-35,-36,-37,-38,-39,-40,-42,-31,61,-44,-41,61,61,-55,-30,61,61,61,-29,-45,-49,61,-48,-43,-46,61,-51,]),'FOR':([16,18,36,43,44,45,46,47,48,49,51,52,56,63,87,88,93,123,124,142,143,147,148,149,153,154,156,157,159,160,],[-6,-7,62,-34,-35,-36,-37,-38,-39,-40,-42,-31,62,-44,-41,62,-55,-30,62,62,62,-29,-45,-49,62,-48,-43,-46,62,-51,]),'DO':([16,18,36,43,44,45,46,47,48,49,51,52,56,63,87,88,93,123,124,142,143,147,148,149,153,154,156,157,159,160,],[-6,-7,63,-34,-35,-36,-37,-38,-39,-40,-42,-31,63,-44,-41,63,-55,-30,63,63,63,-29,-45,-49,63,-48,-43,-46,63,-51,]),'NOTEQUAL':([16,18,36,40,41,43,44,45,46,47,48,49,51,52,56,58,63,64,66,68,70,71,72,75,76,77,78,79,85,87,88,89,90,93,94,95,96,97,98,99,100,101,103,104,113,121,123,124,128,135,136,137,138,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,66,-66,66,-34,-35,-36,-37,-38,-39,-40,-42,-31,66,-91,-44,-96,66,112,-81,-85,-89,-92,-93,-94,-95,-97,66,-41,66,66,66,-55,66,66,66,-62,-63,-64,-65,66,-91,-66,-88,-90,-30,66,66,-80,-84,-67,-98,66,66,66,66,-29,-45,-49,66,-52,66,-48,-43,-46,66,-51,]),'PLUS':([16,18,36,40,41,43,44,45,46,47,48,49,51,52,56,58,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,85,87,88,89,90,93,94,95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,128,134,135,136,137,138,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,73,-66,73,-34,-35,-36,-37,-38,-39,-40,-42,-31,73,-91,-44,-96,73,73,73,-81,-85,-89,-82,-83,-92,-93,-94,-95,-97,73,-41,73,73,73,-55,73,73,73,-62,-63,-64,-65,73,-91,-66,73,73,-74,-75,-76,-77,-78,-79,-88,73,-86,-87,-90,-30,73,73,73,-80,-84,-67,-98,73,73,73,73,-29,-45,-49,73,-52,73,-48,-43,-46,73,-51,]),'MINUS':([16,18,36,40,41,43,44,45,46,47,48,49,51,52,56,58,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,85,87,88,89,90,93,94,95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,121,123,124,128,134,135,136,137,138,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,74,-66,74,-34,-35,-36,-37,-38,-39,-40,-42,-31,74,-91,-44,-96,74,74,74,-81,-85,-89,-82,-83,-92,-93,-94,-95,-97,74,-41,74,74,74,-55,74,74,74,-62,-63,-64,-65,74,-91,-66,74,74,-74,-75,-76,-77,-78,-79,-88,74,-86,-87,-90,-30,74,74,74,-80,-84,-67,-98,74,74,74,74,-29,-45,-49,74,-52,74,-48,-43,-46,74,-51,]),'TRUE':([16,18,36,41,43,44,45,46,47,48,49,51,52,56,63,66,69,73,74,85,87,88,89,90,93,94,95,96,97,98,99,100,101,105,106,107,108,109,110,111,112,114,115,116,123,124,128,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,77,77,-34,-35,-36,-37,-38,-39,-40,-42,-31,77,-44,77,77,-82,-83,77,-41,77,77,77,-55,77,77,77,-62,-63,-64,-65,77,77,77,-74,-75,-76,-77,-78,-79,77,-86,-87,-30,77,77,77,77,77,77,-29,-45,-49,77,-52,77,-48,-43,-46,77,-51,]),'FALSE':([16,18,36,41,43,44,45,46,47,48,49,51,52,56,63,66,69,73,74,85,87,88,89,90,93,94,95,96,97,98,99,100,101,105,106,107,108,109,110,111,112,114,115,116,123,124,128,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,78,78,-34,-35,-36,-37,-38,-39,-40,-42,-31,78,-44,78,78,-82,-83,78,-41,78,78,78,-55,78,78,78,-62,-63,-64,-65,78,78,78,-74,-75,-76,-77,-78,-79,78,-86,-87,-30,78,78,78,78,78,78,-29,-45,-49,78,-52,78,-48,-43,-46,78,-51,]),'NUMBER':([16,18,20,21,36,41,43,44,45,46,47,48,49,51,52,56,63,66,69,73,74,84,85,87,88,89,90,93,94,95,96,97,98,99,100,101,105,106,107,108,109,110,111,112,114,115,116,123,124,128,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,28,30,64,64,-34,-35,-36,-37,-38,-39,-40,-42,-31,64,-44,64,64,-82,-83,117,64,-41,64,64,64,-55,64,64,64,-62,-63,-64,-65,64,64,64,-74,-75,-76,-77,-78,-79,64,-86,-87,-30,64,64,64,64,64,64,-29,-45,-49,64,-52,64,-48,-43,-46,64,-51,]),'FLOAT_NUMBER':([16,18,21,36,41,43,44,45,46,47,48,49,51,52,56,63,66,69,73,74,85,87,88,89,90,93,94,95,96,97,98,99,100,101,105,106,107,108,109,110,111,112,114,115,116,123,124,128,139,142,143,145,147,148,149,150,151,153,154,156,157,159,160,],[-6,-7,31,79,79,-34,-35,-36,-37,-38,-39,-40,-42,-31,79,-44,79,79,-82,-83,79,-41,79,79,79,-55,79,79,79,-62,-63,-64,-65,79,79,79,-74,-75,-76,-77,-78,-79,79,-86,-87,-30,79,79,79,79,79,79,-29,-45,-49,79,-52,79,-48,-43,-46,79,-51,]),'CBRACELET':([16,18,43,44,45,46,47,48,49,51,52,87,88,93,122,123,124,140,141,147,148,149,156,157,160,],[-6,-7,-34,-35,-36,-37,-38,-39,-40,-42,-31,-41,-33,-55,-31,-30,-33,147,-32,-29,-45,-49,-43,-46,-51,]),'RPAREN':([19,25,26,27,33,34,35,40,58,59,64,65,67,68,70,71,72,75,76,77,78,79,80,81,82,83,85,86,102,103,104,113,118,119,120,121,126,127,130,131,132,133,134,135,136,137,138,146,152,155,158,],[-22,36,-21,-24,-25,-27,-28,-66,-91,-61,-96,-69,-71,-73,-81,-85,-89,-92,-93,-94,-95,-97,-23,-26,-59,-60,-100,121,-70,-91,-66,-88,138,-99,-102,-90,142,143,-56,-57,-58,-68,-72,-80,-84,-67,-98,-101,156,-53,159,]),'CLOSEBR':([28,117,],[38,137,]),'PLUSPLUS':([40,],[82,]),'MINUSMINUS':([40,],[83,]),'PLUS_ASSIGN':([40,58,137,],[-66,97,-67,]),'MINUS_ASSIGN':([40,58,137,],[-66,98,-67,]),'TIMES_ASSIGN':([40,58,137,],[-66,99,-67,]),'DIVIDE_ASSIGN':([40,58,137,],[-66,100,-67,]),'TIMES':([40,58,64,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,115,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,115,-84,-67,-98,]),'DIVIDE':([40,58,64,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,116,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,116,-84,-67,-98,]),'EQUALS':([40,58,64,68,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,107,-81,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,-80,-84,-67,-98,]),'LESS':([40,58,64,68,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,108,-81,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,-80,-84,-67,-98,]),'LARGE':([40,58,64,68,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,109,-81,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,-80,-84,-67,-98,]),'LARGETHAN':([40,58,64,68,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,110,-81,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,-80,-84,-67,-98,]),'LESSTHAN':([40,58,64,68,70,71,72,75,76,77,78,79,103,104,113,121,135,136,137,138,],[-66,-91,-96,111,-81,-85,-89,-92,-93,-94,-95,-97,-91,-66,-88,-90,-80,-84,-67,-98,]),'AND':([40,58,59,64,65,67,68,70,71,72,75,76,77,78,79,102,103,104,113,121,133,134,135,136,137,138,],[-66,-91,101,-96,-69,-71,-73,-81,-85,-89,-92,-93,-94,-95,-97,-70,-91,-66,-88,-90,-68,-72,-80,-84,-67,-98,]),'ELSE':([43,44,45,46,47,48,49,51,87,93,147,148,149,156,157,160,],[-34,-35,-36,-37,-38,-39,-40,-42,-41,-55,-29,154,-49,-43,-46,-51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items


_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,11,]),'var_declaration':([0,2,88,91,140,],[4,4,123,128,123,]),'fun_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,19,37,88,91,140,],[6,6,24,24,125,125,125,]),'var_decl_list':([6,125,],[12,12,]),'var_decl_id':([6,17,125,],[15,22,15,]),'params':([19,],[25,]),'param_list':([19,],[26,]),'param_type_list':([19,37,],[27,80,]),'param_id_list':([24,],[33,]),'param_id':([24,39,],[34,81,]),'statement':([36,56,88,124,142,143,153,159,],[42,92,124,124,148,149,157,160,]),'expression_stmt':([36,56,88,124,142,143,153,159,],[43,43,43,43,43,43,43,43,]),'compound_stmt':([36,56,88,124,142,143,153,159,],[44,44,44,44,44,44,44,44,]),'if_stmt':([36,56,88,124,142,143,153,159,],[45,45,45,45,45,45,45,45,]),'while_stmt':([36,56,88,124,142,143,153,159,],[46,46,46,46,46,46,46,46,]),'for_stmt':([36,56,88,124,142,143,153,159,],[47,47,47,47,47,47,47,47,]),'do_while_stmt':([36,56,88,124,142,143,153,159,],[48,48,48,48,48,48,48,48,]),'break_stmt':([36,56,88,124,142,143,153,159,],[49,49,49,49,49,49,49,49,]),'expression':([36,41,56,85,88,89,90,94,95,96,124,128,139,142,143,145,150,153,159,],[50,86,50,120,50,126,127,130,131,132,50,144,146,50,50,152,155,50,50,]),'if':([36,56,88,124,142,143,153,159,],[53,53,53,53,53,53,53,53,]),'while':([36,56,88,92,124,142,143,153,159,],[54,54,54,129,54,54,54,54,54,]),'for':([36,56,88,124,142,143,153,159,],[55,55,55,55,55,55,55,55,]),'do':([36,56,88,124,142,143,153,159,],[56,56,56,56,56,56,56,56,]),'var':([36,41,56,66,69,85,88,89,90,94,95,96,101,105,106,114,124,128,139,142,143,145,150,153,159,],[58,58,58,103,103,58,58,58,58,58,58,58,103,103,103,103,58,58,58,58,58,58,58,58,58,]),'simple_expression':([36,41,56,85,88,89,90,94,95,96,124,128,139,142,143,145,150,153,159,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'unary_rel_expression':([36,41,56,66,85,88,89,90,94,95,96,101,124,128,139,142,143,145,150,153,159,],[65,65,65,102,65,65,65,65,65,65,65,133,65,65,65,65,65,65,65,65,65,]),'rel_expression':([36,41,56,66,85,88,89,90,94,95,96,101,124,128,139,142,143,145,150,153,159,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'add_expression':([36,41,56,66,85,88,89,90,94,95,96,101,105,124,128,139,142,143,145,150,153,159,],[68,68,68,68,68,68,68,68,68,68,68,68,134,68,68,68,68,68,68,68,68,68,]),'addop':([36,41,56,66,68,69,85,88,89,90,94,95,96,101,105,106,114,124,128,134,139,142,143,145,150,153,159,],[69,69,69,69,106,69,69,69,69,69,69,69,69,69,69,69,69,69,69,106,69,69,69,69,69,69,69,]),'term':([36,41,56,66,85,88,89,90,94,95,96,101,105,106,124,128,139,142,143,145,150,153,159,],[70,70,70,70,70,70,70,70,70,70,70,70,70,135,70,70,70,70,70,70,70,70,70,]),'unary_expression':([36,41,56,66,69,85,88,89,90,94,95,96,101,105,106,114,124,128,139,142,143,145,150,153,159,],[71,71,71,71,113,71,71,71,71,71,71,71,71,71,71,136,71,71,71,71,71,71,71,71,71,]),'factor':([36,41,56,66,69,85,88,89,90,94,95,96,101,105,106,114,124,128,139,142,143,145,150,153,159,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'call':([36,41,56,66,69,85,88,89,90,94,95,96,101,105,106,114,124,128,139,142,143,145,150,153,159,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'constant':([36,41,56,66,69,85,88,89,90,94,95,96,101,105,106,114,124,128,139,142,143,145,150,153,159,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'local_declarations':([52,122,],[88,140,]),'addopration_expression':([58,],[95,]),'mulopration_expression':([58,],[96,]),'relop':([68,],[105,]),'mulop':([70,135,],[114,114,]),'args':([85,],[118,]),'args_list':([85,],[119,]),'statement_list':([88,124,],[122,141,]),'semicolon':([144,],[150,]),'else':([148,],[153,]),'epsilon':([155,],[158,]),}


_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),

  ('program -> declaration_list','program',1,'p_program','pp(2).py',284),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list_Loop','pp(2).py',290),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','pp(2).py',296),
  ('declaration -> var_declaration','declaration',1,'p_declaration_var','pp(2).py',302),
  ('declaration -> fun_declaration','declaration',1,'p_declaration_fun','pp(2).py',307),
  ('var_declaration -> type_specifier var_decl_list SEMICOLON','var_declaration',3,'p_var_declaration','pp(2).py',313),
  ('var_declaration -> type_specifier error SEMICOLON','var_declaration',3,'p_var_declaration_error','pp(2).py',323),
  ('var_decl_list -> var_decl_list COMMA var_decl_id','var_decl_list',3,'p_var_decl_list_loop','pp(2).py',328),
  ('var_decl_list -> var_decl_id','var_decl_list',1,'p_var_decl_list','pp(2).py',333),
  ('var_decl_id -> ID','var_decl_id',1,'p_var_decl_id','pp(2).py',339),
  ('var_decl_id -> ID OPENBR NUMBER CLOSEBR','var_decl_id',4,'p_var_decl_array','pp(2).py',345),
  ('var_decl_id -> ID ASSIGN ID','var_decl_id',3,'p_var_decl_ids','pp(2).py',353),
  ('var_decl_id -> ID ASSIGN NUMBER','var_decl_id',3,'p_var_decl_ids','pp(2).py',354),
  ('var_decl_id -> ID ASSIGN FLOAT_NUMBER','var_decl_id',3,'p_var_decl_ids','pp(2).py',355),
  ('var_decl_id -> ID ASSIGN STRING','var_decl_id',3,'p_var_decl_ids','pp(2).py',356),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','pp(2).py',365),
  ('type_specifier -> FLOAT','type_specifier',1,'p_type_specifier','pp(2).py',366),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','pp(2).py',367),
  ('type_specifier -> STRING','type_specifier',1,'p_type_specifier','pp(2).py',368),
  ('fun_declaration -> type_specifier ID LPAREN params RPAREN statement','fun_declaration',6,'p_fun_declaration','pp(2).py',374),
  ('params -> param_list','params',1,'p_params','pp(2).py',382),
  ('params -> <empty>','params',0,'p_params_eps','pp(2).py',387),
  ('param_list -> param_list COMMA param_type_list','param_list',3,'p_param_list__loop','pp(2).py',392),
  ('param_list -> param_type_list','param_list',1,'p_param_list','pp(2).py',397),
  ('param_type_list -> type_specifier param_id_list','param_type_list',2,'p_param_type_list','pp(2).py',402),
  ('param_id_list -> param_id_list COMMA param_id','param_id_list',3,'p_param_id_list_loop','pp(2).py',407),
  ('param_id_list -> param_id','param_id_list',1,'p_param_id_list','pp(2).py',412),
  ('param_id -> ID','param_id',1,'p_param_id','pp(2).py',417),
  ('compound_stmt -> OBRACELET local_declarations statement_list local_declarations CBRACELET','compound_stmt',5,'p_compound_stmt','pp(2).py',422),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations','pp(2).py',429),
  ('local_declarations -> <empty>','local_declarations',0,'p_local_declarations_eps','pp(2).py',434),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','pp(2).py',439),
  ('statement_list -> <empty>','statement_list',0,'p_statement_list_eps','pp(2).py',444),
  ('statement -> expression_stmt','statement',1,'p_statement','pp(2).py',449),
  ('statement -> compound_stmt','statement',1,'p_statement','pp(2).py',450),
  ('statement -> if_stmt','statement',1,'p_statement','pp(2).py',451),
  ('statement -> while_stmt','statement',1,'p_statement','pp(2).py',452),
  ('statement -> for_stmt','statement',1,'p_statement','pp(2).py',453),
  ('statement -> do_while_stmt','statement',1,'p_statement','pp(2).py',454),
  ('statement -> break_stmt','statement',1,'p_statement','pp(2).py',455),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt','pp(2).py',464),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt_eps','pp(2).py',470),
  ('do_while_stmt -> do statement while LPAREN expression RPAREN','do_while_stmt',6,'p_do_while_stmt','pp(2).py',475),
  ('do -> DO','do',1,'p_do','pp(2).py',481),
  ('if_stmt -> if LPAREN expression RPAREN statement','if_stmt',5,'p_if_stmt','pp(2).py',488),
  ('if_stmt -> if LPAREN expression RPAREN statement else statement','if_stmt',7,'p_elif_stmt','pp(2).py',494),
  ('if -> IF','if',1,'p_if','pp(2).py',503),
  ('else -> ELSE','else',1,'p_else','pp(2).py',510),
  ('while_stmt -> while LPAREN expression RPAREN statement','while_stmt',5,'p_while_stmt','pp(2).py',518),
  ('while -> WHILE','while',1,'p_while','pp(2).py',525),
  ('for_stmt -> for LPAREN var_declaration expression semicolon expression epsilon RPAREN statement','for_stmt',9,'p_for_stmt','pp(2).py',534),
  ('semicolon -> SEMICOLON','semicolon',1,'p_semicolon','pp(2).py',542),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','pp(2).py',547),
  ('for -> FOR','for',1,'p_for','pp(2).py',552),
  ('break_stmt -> BREAK SEMICOLON','break_stmt',2,'p_break_stmt','pp(2).py',560),
  ('expression -> var ASSIGN expression','expression',3,'p_expression','pp(2).py',570),
  ('expression -> var addopration_expression expression','expression',3,'p_expression','pp(2).py',571),
  ('expression -> var mulopration_expression expression','expression',3,'p_expression','pp(2).py',572),
  ('expression -> ID PLUSPLUS','expression',2,'p_expression','pp(2).py',573),
  ('expression -> ID MINUSMINUS','expression',2,'p_expression','pp(2).py',574),
  ('expression -> simple_expression','expression',1,'p_expression_simple','pp(2).py',589),
  ('addopration_expression -> PLUS_ASSIGN','addopration_expression',1,'p_addopration_expression','pp(2).py',595),
  ('addopration_expression -> MINUS_ASSIGN','addopration_expression',1,'p_addopration_expression','pp(2).py',596),
  ('mulopration_expression -> TIMES_ASSIGN','mulopration_expression',1,'p_mulopration_expression','pp(2).py',602),
  ('mulopration_expression -> DIVIDE_ASSIGN','mulopration_expression',1,'p_mulopration_expression','pp(2).py',603),
  ('var -> ID','var',1,'p_var','pp(2).py',609),
  ('var -> ID OPENBR NUMBER CLOSEBR','var',4,'p_var_Array','pp(2).py',616),
  ('simple_expression -> simple_expression AND unary_rel_expression','simple_expression',3,'p_simple_expression','pp(2).py',623),
  ('simple_expression -> unary_rel_expression','simple_expression',1,'p_simple_expression_unary','pp(2).py',629),
  ('unary_rel_expression -> NOTEQUAL unary_rel_expression','unary_rel_expression',2,'p_note_unary_rel_expression','pp(2).py',635),
  ('unary_rel_expression -> rel_expression','unary_rel_expression',1,'p_unary_rel_expression','pp(2).py',641),
  ('rel_expression -> add_expression relop add_expression','rel_expression',3,'p_rel_expression','pp(2).py',647),
  ('rel_expression -> add_expression','rel_expression',1,'p_rel_expression_add','pp(2).py',657),
  ('relop -> EQUALS','relop',1,'p_relop','pp(2).py',663),
  ('relop -> LESS','relop',1,'p_relop','pp(2).py',664),
  ('relop -> LARGE','relop',1,'p_relop','pp(2).py',665),
  ('relop -> LARGETHAN','relop',1,'p_relop','pp(2).py',666),
  ('relop -> LESSTHAN','relop',1,'p_relop','pp(2).py',667),
  ('relop -> NOTEQUAL','relop',1,'p_relop','pp(2).py',668),
  ('add_expression -> add_expression addop term','add_expression',3,'p_add_expression','pp(2).py',674),
  ('add_expression -> term','add_expression',1,'p_add_expression_term','pp(2).py',681),
  ('addop -> PLUS','addop',1,'p_addop','pp(2).py',687),
  ('addop -> MINUS','addop',1,'p_addop','pp(2).py',688),
  ('term -> term mulop unary_expression','term',3,'p_term','pp(2).py',695),
  ('term -> unary_expression','term',1,'p_term_unary','pp(2).py',701),
  ('mulop -> TIMES','mulop',1,'p_mulop','pp(2).py',708),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','pp(2).py',709),
  ('unary_expression -> addop unary_expression','unary_expression',2,'p_unary_expression','pp(2).py',715),
  ('unary_expression -> factor','unary_expression',1,'p_unary_expression_fact','pp(2).py',721),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','pp(2).py',727),
  ('factor -> var','factor',1,'p_factor','pp(2).py',728),
  ('factor -> call','factor',1,'p_factor','pp(2).py',729),
  ('factor -> constant','factor',1,'p_factor','pp(2).py',730),
  ('constant -> TRUE','constant',1,'p_constant','pp(2).py',739),
  ('constant -> FALSE','constant',1,'p_constant','pp(2).py',740),
  ('constant -> NUMBER','constant',1,'p_constant_number','pp(2).py',746),
  ('constant -> FLOAT_NUMBER','constant',1,'p_constant_float_number','pp(2).py',752),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','pp(2).py',757),
  ('args -> args_list','args',1,'p_args','pp(2).py',763),
  ('args -> <empty>','args',0,'p_args','pp(2).py',764),
  ('args_list -> args_list COMMA expression','args_list',3,'p_args_list','pp(2).py',769),
  ('args_list -> expression','args_list',1,'p_args_list','pp(2).py',770),

]
