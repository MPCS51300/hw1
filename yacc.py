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

def p_extern(p):
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
    extern : key_extern type globid LPARENTHESES tdecls RPARENTHESES SEMICOLON
           | key_extern type globid LPARENTHESES RPARENTHESES SEMICOLON
    '''

def p_func(p):
    '''
    func : def type globid LPARENTHESES vdecls RPARENTHESES blk
         | def type globid LPARENTHESES RPARENTHESES blk
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
         | return SEMICOLON
         | return exp SEMICOLON
         | vdecl ASSIGN exp SEMICOLON
         | exp SEMICOLON
         | while LPARENTHESES exp RPARENTHESES stmt
         | if LPARENTHESES exp RPARENTHESES stmt else stmt
         | if LPARENTHESES exp RPARENTHESES stmt
         | print exp SEMICOLON
         | print slit SEMICOLON
    '''

def p_exps(p):
    '''
    exps : exp
         | exp COMMA exps
    '''


def p_exp(p):
    '''
    exp : LPARENTHESES exp RPARENTHESES
        | binop
        | uop
        | varid
        | globid LPARENTHESES exps RPARENTHESES
        | globid LPARENTHESES RPARENTHESES
    '''
    #todo:  exp有个branch是lit,但是我不知道lit怎么定义

def p_binop(p):
    '''
    binop : arith-ops
          | logic-ops
          | varid ASSIGN exp
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

def p_globid(p):
    '''
    globid : ident
    '''
    # p[0] = p[1]

def p_type(p):
    '''
    type : int
         | cint
         | float
         | bool
         | void
    '''
    # p[0] = p[1]

def p_refType(p):
    '''
    type : ref type
    '''
    # p[0] = 'ref ' + p[2]

def p_noAliasRefType(p):
    '''
    type : noalias ref type
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
    vdecl : type varid
    '''
    # p[0] = p[1]

parser = yacc.yacc()
while True:
    try:
        s = input('')
    except EOFError:
        break
    # parser.parse(s)
    parser.parse(s, debug=True)
