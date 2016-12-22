# -*- coding: utf-8 -*-

"""
This file is a part of quicksave project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
                   Adam Morawski <poczta@adammorawski.pl>.
"""

from unittest import TestCase

from src.precompiler import precompile, do_main


class PrecompilerTestCase(TestCase):
    def test_precompile(self):
        #with open('input.cc', 'r') as input:
        #    precompile(input.read())
        do_main('input.cc', 'output.cc')