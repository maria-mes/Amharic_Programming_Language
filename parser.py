import ply.yacc as yacc

from lexer import tokens

from ast_nodes import *

# ==========================================
# PRECEDENCE
# ==========================================

precedence = (
    ('left', 'LT', 'GT', 'LTE', 'GTE', 'EQUALS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# ==========================================
# PROGRAM
# ==========================================

def p_program(p):
    '''
    program : statements
    '''

    p[0] = Program(p[1])

# ==========================================
# STATEMENTS
# ==========================================

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    '''
    statements : statement
    '''

    p[0] = [p[1]]

# ==========================================
# BLOCK
# ==========================================

def p_block(p):
    '''
    block : LBRACE statements RBRACE
    '''

    p[0] = p[2]

# ==========================================
# VARIABLE DECLARATION
# ==========================================

def p_statement_var(p):
    '''
    statement : VAR ID ASSIGN expression
    '''

    p[0] = Assignment(p[2], p[4])

# ==========================================
# ASSIGNMENT
# ==========================================

def p_statement_assignment(p):
    '''
    statement : ID ASSIGN expression
    '''

    p[0] = Assignment(p[1], p[3])

# ==========================================
# PRINT
# ==========================================

def p_statement_print(p):
    '''
    statement : PRINT LPAREN expression RPAREN
    '''

    p[0] = Print(p[3])

# ==========================================
# IF
# ==========================================

def p_statement_if(p):
    '''
    statement : IF expression block
    '''

    p[0] = If(
        p[2],
        p[3]
    )

# ==========================================
# IF ELSE
# ==========================================

def p_statement_if_else(p):
    '''
    statement : IF expression block ELSE block
    '''

    p[0] = If(
        p[2],
        p[3],
        p[5]
    )

# ==========================================
# WHILE
# ==========================================

def p_statement_while(p):
    '''
    statement : WHILE expression block
    '''

    p[0] = While(
        p[2],
        p[3]
    )

# ==========================================
# FUNCTION
# ==========================================

def p_statement_function(p):
    '''
    statement : FUNCTION ID LPAREN parameters RPAREN block
    '''

    p[0] = Function(
        p[2],
        p[4],
        p[6]
    )

# ==========================================
# RETURN
# ==========================================

def p_statement_return(p):
    '''
    statement : RETURN expression
    '''

    p[0] = Return(p[2])

# ==========================================
# PARAMETERS
# ==========================================

def p_parameters_multiple(p):
    '''
    parameters : parameters COMMA ID
    '''

    p[0] = p[1] + [p[3]]

def p_parameters_single(p):
    '''
    parameters : ID
    '''

    p[0] = [p[1]]

def p_parameters_empty(p):
    '''
    parameters :
    '''

    p[0] = []

# ==========================================
# ARGUMENTS
# ==========================================

def p_arguments_multiple(p):
    '''
    arguments : arguments COMMA expression
    '''

    p[0] = p[1] + [p[3]]

def p_arguments_single(p):
    '''
    arguments : expression
    '''

    p[0] = [p[1]]

def p_arguments_empty(p):
    '''
    arguments :
    '''

    p[0] = []

# ==========================================
# FUNCTION CALL
# ==========================================

def p_expression_function_call(p):
    '''
    expression : ID LPAREN arguments RPAREN
    '''

    p[0] = FunctionCall(
        p[1],
        p[3]
    )

# ==========================================
# BINARY EXPRESSIONS
# ==========================================

def p_expression_binary(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression LT expression
               | expression GT expression
               | expression LTE expression
               | expression GTE expression
               | expression EQUALS expression
    '''

    p[0] = BinaryOp(
        p[1],
        p[2],
        p[3]
    )

# ==========================================
# NUMBER
# ==========================================

def p_expression_number(p):
    '''
    expression : NUMBER
    '''

    p[0] = Number(p[1])

# ==========================================
# STRING
# ==========================================

def p_expression_string(p):
    '''
    expression : STRING
    '''

    p[0] = String(p[1])

# ==========================================
# IDENTIFIER
# ==========================================

def p_expression_id(p):
    '''
    expression : ID
    '''

    p[0] = Identifier(p[1])

# ==========================================
# GROUPING
# ==========================================

def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN
    '''

    p[0] = p[2]

# ==========================================
# EMPTY
# ==========================================

def p_empty(p):
    '''
    empty :
    '''
    pass

# ==========================================
# ERROR HANDLING
# ==========================================

has_error = False

def p_error(p):

    global has_error

    has_error = True

    if p:

        print(
            f"\nየአገባብ ስህተት (Syntax Error): "
            f"'{p.value}' "
            f"በመስመር {p.lineno}\n"
        )

    else:

        print("\nየአገባብ ስህተት: EOF\n")

# ==========================================
# BUILD PARSER
# ==========================================

parser = yacc.yacc()