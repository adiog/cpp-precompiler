#!/bin/bash

WORKSPACE=`pwd`

function generate_parser()
{
    java -jar ${WORKSPACE}/lib/antlr-4.6-complete.jar \
         -o ${WORKSPACE}/generated \
         -listener \
         -visitor \
         -DcontextSuperClass=PrettyPrintParserRuleContext \
         -Dlanguage=Python3 \
         -lib ${WORKSPACE} \
         ${WORKSPACE}/grammar/CPP14.g4
    touch ${WORKSPACE}/generated/__init__.py
}

function prepend_parser_import_statement()
{
    PARSER=${WORKSPACE}/generated/CPP14Parser.py
    TEMP=`mktemp`
    mv $PARSER $TEMP
    echo "from src.PrettyPrintParserRuleContext import PrettyPrintParserRuleContext" | cat - $TEMP > $PARSER
}

#function make_default_visitor_verbose()
#{
#    VISITOR=${WORKSPACE}/qsql/generated/qsqlVisitor.py
#    VERBOSE_VISITOR=${WORKSPACE}/qsql/generated/qsqlVerboseVisitor.py
#
#    mv $VISITOR $VERBOSE_VISITOR
#    sed -e "s/class qsqlVisitor(ParseTreeVisitor):/class qsqlVerboseVisitor(ParseTreeVisitor):/" -i ${VERBOSE_VISITOR}
##    sed -e "s/.*def visit\([^(]*\)(.*/&\n        print('%s:%s' % ('\L\1\E', ctx.getAltNumber()))/" -i ${VERBOSE_VISITOR}
#}

generate_parser
prepend_parser_import_statement
#make_default_visitor_verbose

