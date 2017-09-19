#!/bin/bash

function generate_parser()
{
    cp grammar/CPP14.g4 .
    java -jar lib/antlr-4.6-complete.jar \
         -o `pwd`/generated \
         -listener \
         -visitor \
         -DcontextSuperClass=PrettyPrintParserRuleContext \
         -Dlanguage=Python3 \
         -lib `pwd` \
         CPP14.g4
    touch generated/__init__.py
    rm CPP14.g4
}

function prepend_parser_import_statement()
{
    PARSER=generated/CPP14Parser.py
    TEMP=`mktemp`
    mv $PARSER $TEMP
    echo "from src.PrettyPrintParserRuleContext import PrettyPrintParserRuleContext" | cat - $TEMP > $PARSER
}

function use_customized_parser() {
    sed -e "s#from .CPP14Parser import CPP14Parser#from generated.CPP14Parser_Custom import CPP14Parser#g" \
    -i \
        generated/CPP14Visitor.py \
        generated/CPP14Listener.py
}

function customize_parser()
{
    (
    echo "import re"
    echo "from src.coroutine_template import COROUTINE_TEMPLATE"
    cat generated/CPP14Parser.py
    ) | sed -e "/class Co_jumpstatementContext/ r parser_parts/class_Co_jumpstatementContext_getText.txt" \
            -e "/class CoroutinedefinitionContext/ r parser_parts/class_CoroutinedefinitionContext_getText.txt" \
            -e "/class YieldexpressionContext/ r parser_parts/class_YieldexpressionContext_getText.txt" > \
            generated/CPP14Parser_Custom.py
}

function fix_parser()
{
    sed -e "/throw new/d" -i generated/CPP14Parser_Custom.py
}

generate_parser
prepend_parser_import_statement
use_customized_parser
customize_parser
fix_parser
