#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
sys.path.append(os.path.dirname(__file__))

from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *
from readability_score.calculators.it.gulpease import *

# If args is empty then fileinput.input() will read from stdin; otherwise it reads from each file in turn
import fileinput

import re

input_text = "".join(fileinput.input())

input_text = input_text.replace("^.*Introduzione.*Introduzione", "")

if len(input_text) > 0:
	gu = Gulpease(input_text, locale='it_IT')
	print gu.readingindex
else:
	print 0


