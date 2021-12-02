'''The words compiler.
'''
import re

from protocol import Pattern

memberRe = re.compile(r'\W*(.+);\W*')


class Member:
  '''The member format of a Cpp class or Golang struct.

  Example:
    '    int a;' -> '    a int'
    '''
  tvpair_pattern: Pattern

  def __init__(self, tvpair_pattern: Pattern):
    self.tvpair_pattern = tvpair_pattern

  def transform(self, source: str):
    tvpair = memberRe.findall(source)[0]

    res_tvpair = self.tvpair_pattern.transform(tvpair)

    return f'    {res_tvpair}'


tvpairRe = re.compile(r'\W*(.+)\W*(.+)\W*')


class TVPair:
  '''The type value pair format.

  Example:
    'int a' -> 'a int'
  '''
  type_pattern: Pattern
  value_pattern: Pattern

  def __init__(self, type_pattern: Pattern, value_pattern: Pattern):
    self.type_pattern = type_pattern
    self.value_pattern = value_pattern

  def transform(self, source: str):
    type, value = tvpairRe.findall(source)[0]  # pylint: disable=redefined-builtin

    res_type = self.type_pattern.transform(type)
    res_value = self.value_pattern.transform(value)

    return f'{res_value} {res_type}'


class TypeDclr:
  '''The type format.

  Example:
    'card_info*' -> '*cardInfo'
  '''
  word_pattern: Pattern

  def __init__(self, word_pattern: Pattern):
    self.word_pattern = word_pattern

  def transform(self, source: str):
    star = '*' if source[-1] == '*' else ''
    words = source[:-1].split('_')

    res_words = [words[0]]
    for word in words[1:]:
      res_words.append(self.word_pattern.transform(word))

    return star + ''.join(res_words)


class Variable:
  '''The variable format.

  Example:
    'card_info' -> 'cardInfo'
  '''
  word_pattern: Pattern

  def __init__(self, word_pattern: Pattern):
    self.word_pattern = word_pattern

  def transform(self, source: str):
    words = source.split('_')

    res_words = [words[0]]
    for word in words[1:]:
      res_words.append(self.word_pattern.transform(word))

    return ''.join(res_words)


class Word:
  '''The word format. Just capital the first character.

  Example:
    'card' -> 'Card'
  '''

  def transform(self, source: str):
    return source[0].upper() + source[1:]


if __name__ == '__main__':
  m = Member(TVPair(
      TypeDclr(Word()),
      Variable(Word()),
  ))
  print(m.transform('    card_type* a_card;'))
