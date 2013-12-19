#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
sys.path.append(os.path.dirname(__file__))

from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *
from readability_score.calculators.it.gulpease import *

# If args is empty then fileinput.input() will read from stdin; otherwise it reads from each file in turn
import fileinput

input_text = "".join(fileinput.input(sys.argv))

fk = FleschKincaid(input_text, locale='it_IT')
dc = DaleChall(input_text, simplewordlist=awordlist, locale='it_IT')
gu = Gulpease(input_text, simplewordlist=awordlist, locale='it_IT')

print fk.min_age
print dc.min_age

