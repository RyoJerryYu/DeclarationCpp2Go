'''Tests for members.py'''
from members import Member
from protocol import DirectReturn


def test_member():
  member_p = Member(DirectReturn())
  assert member_p.transform('    int a;') == '    int a'
