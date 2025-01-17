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


def test_method_default_no_args():
  method_p = Method()
  assert method_p.transform('    uint32 get_type();') == '    GetType() uint32'


def test_method_void_type():
  method_p = Method()
  assert method_p.transform(
      '    void foo(int a, int b);') == '    Foo(a int, b int) '


def test_method_empty_lines():
  method_p = Method()
  assert method_p.transform('\n\n\n    \n') == ''


def test_method_with_const():
  method_p = Method(DirectReturn(), DirectReturn(), DirectReturn())
  assert method_p.transform(
      '    int foo(int a, int b) const ;') == '    foo(int a, int b) int'
