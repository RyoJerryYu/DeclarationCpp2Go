'''The common patterns for the project
'''
import re
from typing import List

from protocol import Pattern

tvpairRe = re.compile(r'\W*([a-zA-Z0-9_\*]+)\W+(\w+)\W*')


class Capitalizer:
  '''The word pattern. Just capital the first character.

  Example:
    'card' -> 'Card'
  '''

  def transform(self, source: str):
    return source[0].upper() + source[1:]


class VarName:
  '''The variable pattern.

  Example:
    'card_info' -> 'cardInfo'
  '''
  word_p: Pattern
  is_public: bool

  def __init__(self, word_p: Pattern = Capitalizer(), is_public: bool = False):
    self.word_p = word_p
    self.is_public = is_public

  def transform(self, source: str):
    words = source.split('_')
    res_words: List[str] = []

    if not self.is_public:
      res_words = [words[0]]
      words = words[1:]

    for word in words:
      res_words.append(self.word_p.transform(word))

    return ''.join(res_words)


class TypeName:
  '''The type pattern.

  Example:
    'card_info*' -> 'CardInfo'
    'card_info' -> 'cardInfo'
  '''
  word_p: Pattern

  def __init__(self, word_p: Pattern = Capitalizer()):
    self.word_p = word_p

  def transform(self, source: str):
    if source == '':
      return ''

    star = ''
    res_words: List[str] = []
    if source.endswith('*'):
      # a pointer will convert into public interface
      words = source[:-1].split('_')
      for word in words:
        res_words.append(self.word_p.transform(word))
    else:
      # normal type will convert into private type
      words = source.split('_')
      res_words.append(words[0])
      for word in words[1:]:
        res_words.append(self.word_p.transform(word))

    return ''.join(res_words)


class TVPair:
  '''The type value pair pattern.

  Example:
    'int a' -> 'a int'
  '''
  type_name_p: Pattern
  var_p: Pattern

  def __init__(self,
               type_name_p: Pattern = TypeName(),
               var_p: Pattern = VarName()):
    self.type_name_p = type_name_p
    self.var_p = var_p

  def transform(self, source: str):
    type, variable = tvpairRe.findall(source)[0]  # pylint: disable=redefined-builtin

    res_type = self.type_name_p.transform(type)
    res_variable = self.var_p.transform(variable)

    return f'{res_variable} {res_type}'
