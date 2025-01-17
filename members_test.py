'''Tests for members.py'''
from members import Member
from protocol import DirectReturn


def test_member():
  member_p = Member(DirectReturn())
  assert member_p.transform('    int a;') == '    int a'


def test_member_default():
  member_p = Member()
  assert member_p.transform('    card* a;') == '    A Card'


def test_member_empty_lines():
  member_p = Member()
  assert member_p.transform('\n\n    \n') == ''
