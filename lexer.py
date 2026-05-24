import ply.lex as lex

# ==========================================
# RESERVED KEYWORDS
# ==========================================

keywords = {

    # Variables
    'ቁጥር': 'VAR',

    # Conditions
    'ከሆነ': 'IF',
    'ያለበለዚያ': 'ELSE',

    # Loops
    'እስከ': 'WHILE',

    # Functions
    'ተግባር': 'FUNCTION',
    'ተመለስ': 'RETURN',

    # Output
    'አትም': 'PRINT',
}

# ==========================================
# TOKEN LIST
# ==========================================

tokens = [

    # Data Types
    'NUMBER',
    'STRING',
    'ID',

    # Arithmetic Operators
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',

    # Assignment
    'ASSIGN',

    # Comparison Operators
    'EQUALS',
    'LT',
    'GT',
    'LTE',
    'GTE',

    # Symbols
    'LPAREN',
    'RPAREN',

    'LBRACE',
    'RBRACE',

    'COMMA',

] + list(keywords.values())

# ==========================================
# SIMPLE TOKENS
# ==========================================

# Arithmetic
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'

# Assignment
t_ASSIGN   = r'='

# Comparisons
t_EQUALS   = r'=='
t_LTE      = r'<='
t_GTE      = r'>='
t_LT       = r'<'
t_GT       = r'>'

# Symbols
t_LPAREN   = r'\('
t_RPAREN   = r'\)'

t_LBRACE   = r'\{'
t_RBRACE   = r'\}'

t_COMMA    = r','

# ==========================================
# STRING TOKEN
# ==========================================

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'

    # Remove quotes
    t.value = t.value[1:-1]

    return t

# ==========================================
# IDENTIFIERS
# Supports:
# - English
# - Amharic Unicode
# ==========================================

def t_ID(t):
    r'[a-zA-Z_ሀ-፼][a-zA-Z0-9_ሀ-፼]*'

    # Check reserved keywords
    t.type = keywords.get(t.value, 'ID')

    return t

# ==========================================
# NUMBERS
# ==========================================

def t_NUMBER(t):
    r'\d+'

    t.value = int(t.value)

    return t

# ==========================================
# COMMENTS
# Example:
#   # this is comment
# ==========================================

def t_COMMENT(t):
    r'\#.*'
    pass

# ==========================================
# IGNORE SPACES/TABS
# ==========================================

t_ignore = ' \t\r'

# ==========================================
# NEWLINES
# ==========================================

def t_newline(t):
    r'\n+'

    t.lexer.lineno += len(t.value)

# ==========================================
# ERROR HANDLING
# ==========================================

def t_error(t):

    print(
        f"\nየቃላት ስህተት (Lexical Error): "
        f"ያልታወቀ ቁምፊ '{t.value[0]}' "
        f"በመስመር {t.lineno}\n"
    )

    t.lexer.skip(1)

# ==========================================
# BUILD LEXER
# ==========================================

lexer = lex.lex()

# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    data = '''

    # variable declaration
    ቁጥር x = 10

    # print
    አትም(x)

    # if statement
    ከሆነ x > 5 {

        አትም("x is greater")

    }

    # while loop
    እስከ x < 15 {

        x = x + 1

    }

    '''

    lexer.input(data)

    print("\n========= TOKENS =========\n")

    while True:

        tok = lexer.token()

        if not tok:
            break

        print(tok)

    print("\n========= END =========\n")