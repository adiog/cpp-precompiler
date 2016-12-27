# -*- coding: utf-8 -*-

"""
This file is a part of cpp-precompiler project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
"""

from io import StringIO

from antlr4 import ParserRuleContext


class PrettyPrintParserRuleContext(ParserRuleContext):
    altNumber = -1

    def getAltNumber(self):
        return self.altNumber

    def setAltNumber(self, alt_number: int):
        self.altNumber = alt_number

    def getText(self):
        if self.getChildCount() == 0:
            return ""
        with StringIO() as builder:
            for child in self.getChildren():
                builder.write(child.getText())
                builder.write(' ')
            return builder.getvalue()

    def getDirtyText(self, children_sequence):
        if children_sequence:
            return list(self.getChildren())[children_sequence[0]].getDirtyText(children_sequence[1:])
        else:
            return self.getText()
