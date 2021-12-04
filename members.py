'''The structure member pattern.
'''
import re
from common import TVPair, TypeName, VarName

from protocol import Pattern

memberRe = re.compile(r'\W*(.+);\W*')


class Member:
  '''The member pattern of a Cpp class or Golang struct.

  Example:
    '    int a;' -> '    a int'
    '''
  tvpair_p: Pattern

  def __init__(self,
               tvpair_p: Pattern = TVPair(TypeName(), VarName(is_public=True))):
    self.tvpair_p = tvpair_p

  def transform(self, source: str):
    tvpair_p = memberRe.findall(source)[0]

    res_tvpair = self.tvpair_p.transform(tvpair_p)

    return f'    {res_tvpair}'
