from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division
from pytest import mark

# content of test_sample.py
def answer1(cmdopt="type1"):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")

@mark.run(order=2)
def test_answer2(cmdopt="type1"):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")

@mark.run(order=1)
def test_answer3(cmdopt="type1"):
    if cmdopt == "type1":
        print("In third procedure")
    elif cmdopt == "type2":
        print("second")

