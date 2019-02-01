import yacc as yacc
import lex as lex


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])

    def getLength(self):
        return self.items.__len__()

    def getPeek(self):
        if self.items.__len__() > 0:
            return self.items.__getitem__(self.items.__len__() - 1)
        else:
            return "none"


symbolTable = []
typestack = Stack()
PB = []
loop = Stack()
index1 = 0
index2 = 0
doindex1 = 0
windex = 0
before_step = 0
after_step = 0
scope_number = 0
temp_counter = 1
label_number = 0
line_number = 1
unique_scope_counter = 0

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'void': 'VOID',
    'break': 'BREAK',
    'true': 'TRUE',
    'false': 'FALSE',
    'do': 'DO'
}
tokens = (
             'LESS',
             'LARGE',
             'ASSIGN',
             'PLUS_ASSIGN',
             'MINUS_ASSIGN',
             'TIMES_ASSIGN',
             'DIVIDE_ASSIGN',
             'NUMBER',
             'FLOAT_NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'OBRACELET',
             'CBRACELET',
             'ID',
             'EQUALS',
             'SEMICOLON',
             'LESSTHAN',
             'LARGETHAN',
             'NOTEQUAL',
             'COMMA',
             'OPENBR',
             'CLOSEBR',
             'AND',
             'PLUSPLUS',
             'MINUSMINUS'
         ) + tuple(reserved.values())

t_AND = r'&'
t_COMMA = r','
t_LESS = r'<='
t_LARGE = r'\>='
t_ASSIGN = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'\-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'\/='
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'=='
t_SEMICOLON = r';'
t_LESSTHAN = r'<'
t_LARGETHAN = r'>'
t_NOTEQUAL = r'!='
t_OPENBR = r'\['
t_CLOSEBR = r'\]'
t_ignore = ' \t'


def add_one():
    global scope_number
    scope_number += 1


def remove_one():
    global scope_number
    scope_number -= 1


def addU_one():
    global temp_counter
    temp_counter += 1


def removeU_one():
    global temp_counter
    temp_counter -= 1


def increment_unique_scope_counter():
    global unique_scope_counter
    unique_scope_counter += 1


def increment_label_number():
    global label_number
    label_number += 1


def decrement_label_number():
    global label_number
    label_number -= 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    global line_number
    line_number += 1


def t_OBRACELET(t):
    r'\{'
    add_one()
    increment_unique_scope_counter()
    return t


def t_CBRACELET(t):
    r'\}'
    remove_one()
    addU_one()
    return t


def t_error(t):
    print("error: Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_STRING(t):
    r'"[a-zA-Z_0-9]*"'
    symbolTable.append([t.type, t.value, id(t.value), scope_number])
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'INT' or t.type == 'STRING' or t.type == 'FLOAT':
        typestack.push(t.type)
        return t

    result = check_table(t.value, scope_number, typestack.getPeek())

    if t.type == 'ID' and not typestack.isEmpty():
        if result == 0:
            symbolTable.append([t.type, t.value, id(t.value), scope_number, typestack.pop(), unique_scope_counter])
    return t


def t_FLOAT_NUMBER(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    symbolTable.append([t.type, t.value, id(t.value), scope_number])
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    symbolTable.append([t.type, t.value, id(t.value), scope_number])
    return t


lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)


def check_table(ch, le, variable_type):
    result = 0
    for m in symbolTable:
        if m[0:1] == ['ID']:
            if ch in m[1:2]:
                if [le] >= m[3:4]:
                    if variable_type == "none" or m[5:6] < [unique_scope_counter]:
                        return 1
                    else:
                        print("error: ", ch, " this used before in this scope line number ", line_number)
                        exit(1)

    return result


def check_assign_table(ch):
    count = 0
    for m in symbolTable:
        if m[0:1] == ['ID']:
            if ch in m[1:2]:
                if [scope_number] >= m[3:4]:
                    count = 1
    if count == 0:
        print(ch, " not defined before  line number ", line_number)
        exit(1)


def typecheck(ch1, ch2):
    type1 = ''
    type2 = ''
    for m in symbolTable:
        if m[0:1] == ['ID']:
            if ch1 in m[1:2]:
                if [scope_number] >= m[3:4]:
                    type1 = m[4:5]
                    break
    for m in symbolTable:
        if m[2:3] == [id(ch2)]:
            type2 = m[0:1]
            break

    if type1 == ['INT'] and type2 != ['NUMBER']:
        print("error : cannot assign ", ch2 ,"to ",ch1)
        exit(1)
    elif type1 == ['FLOAT'] and type2 != ['FLOAT_NUMBER']:
        print("error : cannot assign ", ch2 ,"to ",ch1)
        exit(1)
        type1 == ['STRING'] and type2 != ['STRING']
        print("error : cannot assign ", ch2 ,"to ",ch1)
        exit(1)


def typecheck_for_2id(ch1, ch2):
    type1 = ''
    type2 = ''
    for m in symbolTable:
        if ch1 in m[1:2]:
            if m[0:1] == ['ID']:
                if [scope_number] >= m[3:4]:
                    type1 = m[4:5]
                    break
    for m in symbolTable:
        if ch2 in m[1:2]:
            if m[0:1] == ['ID']:
                if [scope_number] >= m[3:4]:
                    type2 = m[4:5]
                    break
    if type1 != type2 and type2!='':
        print("error: type error line number ", line_number)
        exit(1)


def generate_code(action, p1, p3):
    if action == '=':
        PB.append(['=', p3, p1])
    elif action == '*':
        PB.append(['*', p1, p3, 'temp' + str(temp_counter)])
    elif action == '/':
        PB.append(['/', p1, p3, 'temp' + str(temp_counter)])
    elif action == '+':
        PB.append(['+', p1, p3, 'temp' + str(temp_counter)])
    elif action == '-':
        PB.append(['-', p1, p3, 'temp' + str(temp_counter)])
    return 'temp' + str(temp_counter)


def p_program(p):
    'program : declaration_list'
    p[0] = p[1]
    print("p_program")


def p_declaration_list_Loop(p):
    'declaration_list : declaration_list declaration'
    p[0] = (p[1], p[2])
    print("p_declaration_list_Loop")


def p_declaration_list(p):
    'declaration_list : declaration'
    p[0] = p[1]
    print("p_declaration_list")


def p_declaration_var(p):
    'declaration : var_declaration'
    print("p_declaration_var")


def p_declaration_fun(p):
    'declaration : fun_declaration'
    p[0] = p[1]
    print("p_declaration_fun")


def p_var_declaration(p):
    '''var_declaration : type_specifier var_decl_list SEMICOLON'''
    if p[1] == 'void':
        print("error: void cant use for this")
        exit(1)
    p[0] = p[2]
    print("p_var_declaration", p[1], p[2])


def p_var_declaration_error(p):
    'var_declaration : type_specifier error SEMICOLON'
    print("error: type error cant be string", line_number, p[1])


def p_var_decl_list_loop(p):
    'var_decl_list : var_decl_list COMMA var_decl_id'
    print("p_var_decl_list_loop")


def p_var_decl_list(p):
    'var_decl_list : var_decl_id'
    p[0] = p[1]
    print("p_var_decl_list")


def p_var_decl_id(p):
    'var_decl_id : ID'
    p[0] = p[1]
    print("p_var_decl_id", p[1])


def p_var_decl_array(p):
    'var_decl_id : ID OPENBR NUMBER CLOSEBR'
    print("p_var_decl_array")


def p_var_decl_ids(p):
    '''var_decl_id : ID ASSIGN NUMBER
        | ID ASSIGN FLOAT_NUMBER
        | ID ASSIGN STRING'''
    typecheck(p[1], p[3])
    PB.append([p[2], p[3], p[1]])
    p[0] = p[1]
    print("p_var_decl_ids")


def p_var_decl_assign_ids(p):
    'var_decl_id : ID ASSIGN ID'
    check_assign_table(p[1])
    check_assign_table(p[3])
    typecheck_for_2id(p[1], p[3])
    PB.append([p[2], p[3], p[1]])
    p[0] = p[3]
    print("p_var_decl_assign_ids")


def p_type_specifier(p):
    '''type_specifier : INT
    | FLOAT
    | VOID
    | STRING'''
    p[0] = p[1]
    print("p_type_specifier", p[1])


def p_fun_declaration(p):
    '''fun_declaration : type_specifier ID LPAREN params RPAREN statement'''
    check_assign_table(p[2])
    p[0] = p[6]
    print("p_fun_declaration " + p[1])


def p_params(p):
    'params : param_list'
    print("p_params")


def p_params_eps(p):
    'params : '
    # print("p_params_eps")


def p_param_list__loop(p):
    'param_list : param_list COMMA param_type_list '
    # print("p_param_list__loop")


def p_param_list(p):
    'param_list : param_type_list'
    # print("p_param_list")


def p_param_type_list(p):
    '''param_type_list : type_specifier param_id_list'''
    # print("p_param_type_list")


def p_param_id_list_loop(p):
    'param_id_list : param_id_list COMMA param_id'
    # print("p_param_id_list_loop")


def p_param_id_list(p):
    'param_id_list : param_id'
    # print("p_param_id_list")


def p_param_id(p):
    'param_id : ID'
    print("p_param_id")


def p_compound_stmt(p):
    'compound_stmt : OBRACELET local_declarations statement_list local_declarations CBRACELET'
    p[0] = p[3]
    print("p_compound_stmt")


def p_local_declarations(p):
    'local_declarations : local_declarations var_declaration'
    print("p_local_declarations")


def p_local_declarations_eps(p):
    'local_declarations :'
    print("p_local_declarations_eps")


def p_statement_list(p):
    'statement_list : statement statement_list'
    print("p_statement_list", scope_number)


def p_statement_list_eps(p):
    'statement_list :'
    print("p_statement_list_eps")


def p_statement(p):
    '''statement : expression_stmt
    | compound_stmt
    | if_stmt
    | while_stmt
    | for_stmt
    | do_while_stmt
    | break_stmt'''
    print("p_statement")


def p_expression_stmt(p):
    'expression_stmt : expression SEMICOLON'
    p[0] = p[1]
    print("p_expression_stmt")


def p_expression_stmt_eps(p):
    'expression_stmt : SEMICOLON'
    print("p_expression_stmt_eps")


def p_do_while_stmt(p):
    'do_while_stmt : do statement while LPAREN expression RPAREN'
    PB.append(["JPT", p[5][3], doindex1 + 1])
    p[0] = p[5]


def p_do(p):
    'do : DO'
    global doindex1
    doindex1 = len(PB)
    loop.push(p[1])
    # print("p_do")


def p_if_stmt(p):
    'if_stmt : if LPAREN rel_expression RPAREN statement'
    PB.insert(index1 + 1, ["JPF", p[3][3], len(PB) + 2])
    increment_label_number()
    print("p_if_stmt")


def p_elif_stmt(p):
    'if_stmt : if LPAREN rel_expression RPAREN statement else statement'
    PB.insert(index1 + 1, ["JPF", p[3][3], index2 + 2])
    t = len(PB) - index2  #else statement size
    PB.insert(len(PB) - t, ["JP", len(PB) + 2, ])
    increment_label_number()
    # print("p_elif_stmt")


def p_if(p):
    'if : IF'
    global index1
    index1 = len(PB)
    print("p_if")


def p_else(p):
    'else : ELSE '
    global index2
    index2 = len(PB) + 1
    # name="else"
    print("p_else")


def p_while_stmt(p):
    '''while_stmt : while LPAREN rel_expression RPAREN statement'''
    PB.insert(windex1 + 1, ["JPF", p[3][3], len(PB) + 2])
    loop.pop()
    print("p_while_stmt", id(p[1]))


def p_while(p):
    'while : WHILE'
    loop.push(p[1])
    global windex1
    windex1 = len(PB)
    print("p_while", id(p[0]))





def p_for_stmt(p):
    '''for_stmt : for LPAREN var_declaration rel_expression semicolon expression epsilon RPAREN statement'''
    m = before_step
    while (after_step - m > 0):
        PB.append(PB.pop(before_step))
        m += 1

    PB.insert(before_step, ['JPF', p[4][3], len(PB) + 3])
    PB.append(['JP', after_step - 2, ])

    p[0] = p[8]
    loop.pop()
    print("p_for_stmt")


def p_semicolon(p):
    'semicolon : SEMICOLON'
    global before_step
    before_step = len(PB)


def p_epsilon(p):
    'epsilon :'
    global after_step
    after_step = len(PB)


def p_for(p):
    'for : FOR'
    loop.push(p[1])
    print("p_for")


def p_break_stmt(p):
    'break_stmt : BREAK SEMICOLON'
    if loop.isEmpty():
        print("error: semantic error in break")
        exit(1)
    p[0] = p[1]

    print("p_break_stmt")


def p_expression(p):
    ''' expression : var ASSIGN expression
      | var addopration_expression expression
      | var mulopration_expression expression
      | ID PLUSPLUS
      | ID MINUSMINUS
      '''
    check_assign_table(p[1])
    if p[3]=="NUMBER" or p[3]=="STRING" or p[3]=="ID":
        typecheck(p[1], p[3])
        typecheck_for_2id(p[1], p[3])
    if p[2] == '=':
        p[0] = generate_code('=', p[1], p[3], )
    print("p_expression", p[1], p[2], p[3])


def p_expression_simple(p):
    'expression : simple_expression '
    p[0] = p[1]
    print("p_expression_simple")


def p_addopration_expression(p):
    ''' addopration_expression : PLUS_ASSIGN
    | MINUS_ASSIGN'''
    p[0] = p[1]
    print("p_addopration_expression")


def p_mulopration_expression(p):
    ''' mulopration_expression : TIMES_ASSIGN
    | DIVIDE_ASSIGN'''
    p[0] = p[1]
    print("p_mulopration_expression")


def p_var(p):
    'var : ID'
    check_assign_table(p[1])
    p[0] = p[1]
    print("p_var", p[1])


def p_var_Array(p):
    'var : ID OPENBR NUMBER CLOSEBR'
    # check_assign_table(p[1])
    p[0] = (" ARRAY ", p[1], " SIZE: ", p[3])
    print("p_var_Array")


def p_simple_expression(p):
    'simple_expression : simple_expression AND unary_rel_expression'
    # p[0]=(p[1],p[3])
    print("p_simple_expression")


def p_simple_expression_unary(p):
    'simple_expression : unary_rel_expression'
    p[0] = p[1]
    print("p_simple_expression_unary")


def p_note_unary_rel_expression(p):
    'unary_rel_expression : NOTEQUAL unary_rel_expression'
    # p[0]=('!',p[1])
    print("p_note_unary_rel_expression")


def p_unary_rel_expression(p):
    'unary_rel_expression : rel_expression'
    p[0] = p[1]
    print("p_unary_rel_expression")


def p_rel_expression(p):
    'rel_expression :  add_expression relop add_expression '
    PB.append([p[2], p[1], p[3], 'temp' + str(temp_counter)])
    p[0] = [p[2], p[1], p[3], 'temp' + str(temp_counter)]
    if_index1 = len(PB)
    addU_one()
    # generate_code(p[2], p[1], p[3])
    print("p_rel_expression")


def p_rel_expression_add(p):
    'rel_expression : add_expression'
    p[0] = p[1]
    print("p_rel_expression_add")


def p_relop(p):
    '''relop : EQUALS
                  | LESS
                  | LARGE
                  | LARGETHAN
                  | LESSTHAN
                  | NOTEQUAL'''
    p[0] = p[1]
    print("p_relop")


def p_add_expression(p):
    '''add_expression : add_expression addop term '''
    addU_one()
    p[0] = generate_code(p[2], p[1], p[3])
    print("p_add_expression")


def p_add_expression_term(p):
    '''add_expression : term'''
    p[0] = p[1]
    print("p_add_expression_term")


def p_addop(p):
    '''addop : PLUS
            | MINUS
            '''
    p[0] = p[1]
    print("p_addop")


def p_term(p):
    'term : term mulop unary_expression '
    p[0] = generate_code(p[2], p[1], p[3])
    print("p_term")


def p_term_unary(p):
    'term : unary_expression'
    p[0] = p[1]
    print("p_term_unary")


def p_mulop(p):
    '''mulop : TIMES
            | DIVIDE'''
    p[0] = p[1]
    print("p_mulop")


def p_unary_expression(p):
    'unary_expression : addop unary_expression'
    p[0] = (p[1], p[2])
    print("p_unary_expression")


def p_unary_expression_fact(p):
    'unary_expression : factor'
    p[0] = p[1]
    print("p_unary_expression_fact")


def p_factor(p):
    '''factor : LPAREN expression RPAREN
    | var
    | call
    | constant'''
    if p[1] == '(':
        p[0] = (p[2])
    else:
        p[0] = p[1]
    print("p_factor")


def p_constant(p):
    '''constant : TRUE
    | FALSE'''
    p[0] = p[1]
    print("p_constant")


def p_constant_number(p):
    'constant : NUMBER '
    p[0] = p[1]
    print("p_constant_number")


def p_constant_string(p):
    'constant : STRING '
    p[0] = p[1]
    print("p_constant_string")


def p_constant_float_number(p):
    'constant : FLOAT_NUMBER '
    p[0] = p[1]


def p_call(p):
    '''call : ID LPAREN args RPAREN'''
    check_assign_table(p[1])
    # p[0] = ('CALL', p[1], "args=", p[3])
    print("p_call")


def p_args(p):
    '''args : args_list
    |'''
    # print("p_args")


def p_args_list(p):
    '''args_list : args_list COMMA expression
    | expression'''
    # print("p_args_list")


def p_error(p):
    print("error: Syntax error at '%s'" % p.value, "line number ", line_number)


yacc.yacc()
if __name__ == "__main__":
    file = open("example/input.txt", "r")
    data = file.read()
    res = yacc.parse(data)
    print("********************************************************\n")
    k = 0
    for m in PB:
        k += 1
        print(m, "\n")
    print("**********************************************************\n")
    k = 0;
    for m in PB:
        k += 1
        if m[0] == '=':
            print("message: ", k, "->", str(m[2]) + " " + str(m[0]) + " " + str(m[1]))
        elif m[0] == 'JPF':
            print("message: ", k, "->", str(m[0]) + " " + str(m[1]) + " " + str(m[2]))
        elif m[0] == 'JP':
            print("message: ", k, "->", str(m[0]) + " " + str(m[1]))
        else:
            print("message: ", k, "->", str(m[3]) + " = " + str(m[1]) + " " + str(m[0]) + " " + str(m[2]))

    print("message: ", k+1, "-> halt")