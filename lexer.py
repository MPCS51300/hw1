import ply.lex as lex

reserved = {
    'int' : 'INT',
    'cint' : 'CINT',
    'float' : 'FLOAT',
    'bool' : 'BOOL',
    'void' : 'VOID',
    'ref' : 'REF',
    'noalias' : 'NOALIAS',
    'return' : 'RETURN',
    'while' : 'WHILE',
    'if' : 'IF',
    'else' : 'ELSE',
    'print' : 'PRINT',
    'def' : 'DEF',
    "extern" : 'EXTERN',
    "true" : 'TRUE',
    "false" : 'FALSE'
 }

tokens = list(reserved.values()) + [
    #number and boolean
    'NUMBER', 'FNUMBER',
    # arithmetic
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    # compare
    'EQUAL', 'GREATERTHAN', 'SMALLERTHAN', 
    # logical operations
    'AND', 'OR', 'NEGATE',
    # (),{},[]
    'LPARENTHESES', 'RPARENTHESES', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    # delimiter
    'COMMA', 'SEMICOLON',
    # slit
    'slit',
    # ident
    'ident',
    # varid
    'varid'
]

# arithmetic
t_PLUS = r"\+"
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r'\='
# compare
t_EQUAL = r'\=\='
t_GREATERTHAN = r'\>'
t_SMALLERTHAN = r'\<'
# logical operations
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NEGATE = r'\!'
# (),{},[]
t_LPARENTHESES = r'\('
t_RPARENTHESES = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
# delimiter
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

t_ignore  = ' \t'

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

def t_slit(t):
    r'[^"\n\r]*'
    return t

def t_ident(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, "ident")
    return t

def t_varid(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'[-+]?\d+'
    t.value = int(t.value)
    return t

def t_FNUMBER(t):
    r'[-+]?[0-9]*\.?[0-9]+'
    t.value = float(t.value)
    return t 

lexer = lex.lex()