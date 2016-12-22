# -*- coding: utf-8 -*-

"""
This file is a part of cpp-precompiler project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
"""
import os
from unittest import TestCase

from src.precompiler import precompile, do_main


class PrecompilerTestCase(TestCase):
    def test_precompile(self):
        do_main('input.cc', 'output.cc')
        os.system('clang-format -i output.cc')