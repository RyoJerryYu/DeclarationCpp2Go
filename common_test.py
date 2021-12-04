'''Tests for common.py'''
from common import Capitalizer, TVPair, TypeName, VarName
from protocol import DirectReturn


def test_capitalizer():
  capitalizer = Capitalizer()
  assert capitalizer.transform('card') == 'Card'


def test_varname():
  varname = VarName(Capitalizer())
  assert varname.transform('card_info') == 'cardInfo'


def test_varname_default():
  varname = VarName()
  assert varname.transform('card_info') == 'cardInfo'


def test_varname_public():
  varname = VarName(Capitalizer(), is_public=True)
  assert varname.transform('card_info') == 'CardInfo'


def test_typename_pointer():
  typename = TypeName(Capitalizer())
  assert typename.transform('card_info*') == 'CardInfo'


def test_typename_not_pointer():
  typename = TypeName(Capitalizer())
  assert typename.transform('card_info') == 'cardInfo'


def test_typename_default():
  typename = TypeName()
  assert typename.transform('card_info*') == 'CardInfo'


def test_typename_empty():
  typename = TypeName(Capitalizer())
  assert typename.transform('') == ''


def test_tvpair():
  tvpair_p = TVPair(DirectReturn(), DirectReturn())
  assert tvpair_p.transform('int a') == 'a int'


def test_tvpair_default():
  tvpair_p = TVPair()
  assert tvpair_p.transform('int a') == 'a int'
