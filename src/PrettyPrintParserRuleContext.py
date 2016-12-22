# -*- coding: utf-8 -*-

"""
This file is a part of quicksave project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
                   Adam Morawski <poczta@adammorawski.pl>.
"""

#from StringIO import StringIO
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

    def getDirtyText(self, list_no):
        if list_no:
            return list(self.getChildren())[list_no[0]].getDirtyText(list_no[1:])
        else:
            return self.getText()
