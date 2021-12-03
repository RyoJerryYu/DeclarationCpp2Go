'''The class method compiler
'''

import re
from typing import List
from protocol import Pattern

methodRe = re.compile(r'\W*([a-zA-Z0-9_\*]+)\W+(\w+)\((.*)\);\W*')


class Method:
  '''The class method compiler
    '''
  type_name: Pattern
  fname: Pattern
  tvlist: Pattern

  def __init__(self, type_name: Pattern, fname: Pattern, tvlist: Pattern):
    self.type_name = type_name
    self.fname = fname
    self.tvlist = tvlist

  def transform(self, source: str) -> str:
    type, func, tvlist = methodRe.findall(source)[0]  # pylint: disable=redefined-builtin

    res_type = self.type_name.transform(type)
    res_func = self.fname.transform(func)
    res_tvlist = self.tvlist.transform(tvlist)

    return f'    {res_func}({res_tvlist}) {res_type}'


class FuncName:
  '''The function name compiler
  '''
  word_p: Pattern

  def __init__(self, word_p: Pattern):
    self.word_p = word_p

  def transform(self, source: str) -> str:
    words = source.split('_')

    res_words: List[str] = []
    for word in words:
      res_words.append(self.word_p.transform(word))

    return ''.join(res_words)


class TVList:
  '''The type variable list compiler
  '''
  tvpair_p: Pattern

  def __init__(self, tvpair_p: Pattern):
    self.tvpair_p = tvpair_p

  def transform(self, source: str) -> str:
    tvpairs = [x.strip() for x in source.split(',')]

    res_tvpairs: List[str] = []
    for tvpair in tvpairs:
      res_tvpairs.append(self.tvpair_p.transform(tvpair))

    return ', '.join(res_tvpairs)
