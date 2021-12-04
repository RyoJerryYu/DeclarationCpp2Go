'''Tests for methods.py'''
from methods import FuncName, Method, TVList
from common import Capitalizer
from protocol import DirectReturn


def test_funcname():
  funcname_p = FuncName(Capitalizer())
  assert funcname_p.transform('foo_bar_baz') == 'FooBarBaz'


def test_funcname_default():
  funcname_p = FuncName()
  assert funcname_p.transform('foo_bar_baz') == 'FooBarBaz'


def test_tvlist():
  tvlist_p = TVList(DirectReturn())
  assert tvlist_p.transform('int a, int b') == 'int a, int b'


def test_tvlist_default():
  tvlist_p = TVList()
  assert tvlist_p.transform('int a, int b') == 'a int, b int'


def test_method():
  method_p = Method(DirectReturn(), DirectReturn(), DirectReturn())
  assert method_p.transform(
      '    int foo(int a, int b);') == '    foo(int a, int b) int'


def test_method_default():
  method_p = Method()
  assert method_p.transform(
      '    int foo(int a, int b);') == '    Foo(a int, b int) int'
