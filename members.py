'''The words compiler.
'''
import re

from protocol import Pattern

memberRe = re.compile(r'\W*(.+);\W*')


class Member:
  '''The member pattern of a Cpp class or Golang struct.

  Example:
    '    int a;' -> '    a int'
    '''
  tvpair_p: Pattern

  def __init__(self, tvpair_p: Pattern):
    self.tvpair_p = tvpair_p

  def transform(self, source: str):
    tvpair_p = memberRe.findall(source)[0]

    res_tvpair = self.tvpair_p.transform(tvpair_p)

    return f'    {res_tvpair}'


tvpairRe = re.compile(r'\W*([a-zA-Z0-9_\*]+)\W+(\w+)\W*')


class TVPair:
  '''The type value pair pattern.

  Example:
    'int a' -> 'a int'
  '''
  type_name_p: Pattern
  var_p: Pattern

  def __init__(self, type_name_p: Pattern, var_p: Pattern):
    self.type_name_p = type_name_p
    self.var_p = var_p

  def transform(self, source: str):
    type, variable = tvpairRe.findall(source)[0]  # pylint: disable=redefined-builtin

    res_type = self.type_name_p.transform(type)
    res_variable = self.var_p.transform(variable)

    return f'{res_variable} {res_type}'


class TypeName:
  '''The type pattern.

  Example:
    'card_info*' -> '*cardInfo'
  '''
  word_p: Pattern

  def __init__(self, word_p: Pattern):
    self.word_p = word_p

  def transform(self, source: str):
    star = '*' if source[-1] == '*' else ''
    words = source[:-1].split('_')

    res_words = [words[0]]
    for word in words[1:]:
      res_words.append(self.word_p.transform(word))

    return star + ''.join(res_words)


class Variable:
  '''The variable pattern.

  Example:
    'card_info' -> 'cardInfo'
  '''
  word_p: Pattern

  def __init__(self, word_p: Pattern):
    self.word_p = word_p

  def transform(self, source: str):
    words = source.split('_')

    res_words = [words[0]]
    for word in words[1:]:
      res_words.append(self.word_p.transform(word))

    return ''.join(res_words)


class Capitalizer:
  '''The word pattern. Just capital the first character.

  Example:
    'card' -> 'Card'
  '''

  def transform(self, source: str):
    return source[0].upper() + source[1:]


if __name__ == '__main__':
  m = Member(TVPair(
      TypeName(Capitalizer()),
      Variable(Capitalizer()),
  ))
  print(m.transform('    card_type* a_card;'))
