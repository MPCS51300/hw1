import ply.yacc as yacc
import lexer
tokens = lexer.tokens 

#######
# Parser
#######

def p_prog(p):
    '''
    prog : externs funcs
    '''

def p_externs(p):
    '''
    externs : 
             | extern
             | extern externs
    '''

def p_funcs(p):
    '''
    funcs : func
          | func funcs
    '''

def p_extern(p):
    '''
    extern : EXTERN type globid LPARENTHESE tdecls RPARENTHESE SEMICOLON
           | EXTERN type globid LPARENTHESE RPARENTHESE SEMICOLON
    '''

def p_func(p):
    '''
    func : DEF type globid LPARENTHESE vdecls RPARENTHESE blk
         | DEF type globid LPARENTHESE RPARENTHESE blk
    '''

def p_blk(p):
    '''
    blk : LBRACE stmts RBRACE
        | LBRACE RBRACE
     '''

def p_stmts(p):
    '''
    stmts : stmt
          | stmt stmts
    '''

def p_stmt(p):
    '''
    stmt : blk
         | RETURN SEMICOLON
         | RETURN exp SEMICOLON
         | vdecl ASSIGN exp SEMICOLON
         | exp SEMICOLON
         | WHILE LPARENTHESE exp RPARENTHESE stmt
         | IF LPARENTHESE exp RPARENTHESE stmt ELSE stmt
         | IF LPARENTHESE exp RPARENTHESE stmt
         | PRINT exp SEMICOLON
         | PRINT SLIT SEMICOLON
    '''

def p_exps(p):
    '''
    exps : exp
         | exp COMMA exps
    '''

def p_exp(p):
    '''
    exp : LPARENTHESE exp RPARENTHESE
        | binop
        | uop
        | lit
        | VARID
        | globid LPARENTHESE exps RPARENTHESE
        | globid LPARENTHESE RPARENTHESE
    '''

def p_binop(p):
    '''
    binop : arith-ops
          | logic-ops
          | VARID ASSIGN exp
          | LBRACKET type RBRACKET exp
    '''

def p_arithOps(p):
    '''
    arith-ops : exp TIMES exp
              | exp DIVIDE exp
              | exp PLUS exp
              | exp MINUS exp
    '''

def p_logicOps(p):
    '''
    logic-ops : exp EQUAL exp
              | exp SMALLERTHAN exp
              | exp GREATERTHAN exp
              | exp AND exp
              | exp OR exp
    '''

def p_uop(p):
    '''
    uop : NEGATE exp 
        | MINUS exp
    '''

def p_lit(p):
    '''
    lit : true
        | false
        | FNUMBER
        | NUMBER
    '''

def p_true(p):
    '''
    true : TRUE
    '''

def p_false(p):
    '''
    false : FALSE
    '''

def p_globid(p):
    '''
    globid : IDENT
    '''
    # p[0] = p[1]

def p_type(p):
    '''
    type : INT
         | CINT
         | FLOAT
         | BOOL
         | VOID
    '''
    # p[0] = p[1]

def p_refType(p):
    '''
    type : REF type
    '''
    # p[0] = 'ref ' + p[2]

def p_noAliasRefType(p):
    '''
    type : NOALIAS REF type
    '''
    # p[0] = 'noalias ref ' + p[3]

def p_vdecls(p):
    '''
    vdecls : vdecl
           | vdecl COMMA vdecls
    '''
    # if len(p) == 2:
    #     p[0] = p[1]
    # else :
    #     p[0] = (p[1], p[3])

def p_tdecls(p):
    '''
    tdecls : type
           | type COMMA tdecls
    '''
    # if len(p) == 2:
    #     p[0] = p[1]
    # else :
    #     p[0] = (p[1], ',', p[3])

def p_vdecl(p):
    '''
    vdecl : type VARID
    '''
    # p[0] = p[1]

parser = yacc.yacc()

with open('test/test1.ek', 'r') as content_file:
    content = content_file.read()
    parser.parse(content, debug=True)