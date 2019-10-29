import argparse

import sys
sys.path.insert(0, './')

import lexer
import yacc

parser = argparse.ArgumentParser(prog=sys.argv[0], usage="./bin/ekcc[.py] [-h|-?] [-v] [-O] [-emit-ast|-emit-llvm] -o <output-file> <input-file>", add_help=False)
parser.add_argument("-h", action="help", help="show this help message and exit")
parser.add_argument("-v", help="print information for debugging", default=False)
parser.add_argument("-O", help="enable optimization", default=False)
parser.add_argument("-emit-ast", help="dump AST in a YAML format", default=False)
parser.add_argument("-emit-llvm", help="output LLVM IR", default=False)
parser.add_argument("-o", help="set output file path", default=sys.stdout)
args, unknown = parser.parse_known_args()

if len(unknown) != 1:
    raise ValueError("Usage: ./bin/ekcc.py <input_file>")
else:
    with open(unknown[0], 'r') as input:  
        content = input.read()
        result = yacc.parse(content)
        if isinstance(args.o, str):
            with open(args.o, 'w') as output:
                output.write(result)
        else:
            args.o.write(result)