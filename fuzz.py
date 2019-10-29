import afl, yacc, lexer
import os, sys

afl.init()
sys.stdin.seek(0)
content = sys.stdin.read()
result = yacc.parser.parse(content, debug=True)
os._exit(0)
