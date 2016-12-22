# -*- coding: utf-8 -*-

"""
This file is a part of quicksave project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
                   Adam Morawski <poczta@adammorawski.pl>.
"""
import sys

import re
from antlr4 import InputStream

from generated.CPP14Lexer import CPP14Lexer, CommonTokenStream
from generated.CPP14Parser import CPP14Parser
from generated.CPP14Visitor import CPP14Visitor


def is_source_valid(source):
    input_file = InputStream(source)
    lexer = CPP14Lexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationunit()
    return parser._syntaxErrors == 0

def precompile(source):
    if not is_source_valid(source):
        raise RuntimeError()
    input_file = InputStream(source)
    lexer = CPP14Lexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationunit()
    visitor = CPP14Visitor()
    visitor.visit(tree)
    print(tree.getText())
    return re.sub(r'<EOF>', '', tree.getText())

def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    do_main(input_filename, output_filename)

def do_main(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        with open(output_filename, 'w') as output_file:
            output_file.write(precompile(input_file.read()))



if __name__ == '__main__':
    main()