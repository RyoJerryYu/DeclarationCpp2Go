'''Pattern Protocol

    Define the protocol for all the pattern could be
    transform from Cpp to Golang.
'''
from typing import Protocol


class Pattern(Protocol):

  def transform(self, data: str) -> str:
    ...


class DirectReturn:

  def transform(self, data: str) -> str:
    return data
